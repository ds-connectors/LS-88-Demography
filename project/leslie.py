from datascience import *

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


_unpd_asfr = Table.read_table('../data/UNPD/unpd_asfr_cleaned.csv')
_unpd_lt = Table.read_table('../data/UNPD/unpd_life_tables_cleaned.csv')
_unpd_pop = Table.read_table('../data/UNPD/unpd_f_pop_byage_cleaned.csv')

all_ages = np.unique(_unpd_pop['age'])

def get_lt(country, period, sex='female'):
    """
    This function reads in the life table data for a given country and time period.
    """
    lt_data = _unpd_lt.where('area', country).where('period', period).where('sex', sex)
    return(lt_data.sort('age'))

def get_asfr(country, period):
    asfr_data = _unpd_asfr.where('area', country).where('period', period)
    # rescale rates (which are listed per 1,000 in the UNPD data)
    asfr_data = asfr_data.with_column('asfr', asfr_data['asfr']/1000)
    return(asfr_data.sort('age'))

def get_pop(country, reference_date):
    raw_dat = _unpd_pop.where('area', country).where('reference_date', reference_date)
    return(raw_dat)

def get_pop_vec(country, reference_date):
    dat = get_pop(country, reference_date)
    
    # collapse last two age groups to get 75+ to match our Leslie matrices
    #pop_vec = dat.column('f_population')[:-2]
    #pop_vec = np.append(pop_vec, np.sum(dat.column('f_population')[-2:]))
    pop_vec = dat.column('f_population')
    
    return(pop_vec)



def normalize_distn(pops):
    return(pops / np.sum(pops))

def make_leslie_matrix(country, period):
    lt = get_lt(country, period, 'female')
    asfr = get_asfr(country, period)

    return(build_leslie_matrix(lt, asfr))

def build_leslie_matrix(lt, asfr):

    """
    This function was designed to keep things (fairly) simple, and to work with the UNPD data
    we're using in the connector class.
    
    We'll project populations up to 75+, since that is easiest with the age group info that UNPD provides.
    """
    
    # we'll collapse the youngest two age groups
    # AND the oldest two age groups, so the number of age groups in the Leslie matrix
    # will be 2 fewer than the number of rows in the life table
    num_ages = lt.num_rows - 2
    leslie_mat = np.zeros(shape=(num_ages, num_ages))
    
    ##############################
    ## calculate survivorship (subdiagonal of Leslie matrix)
    ##############################
    
    # the first two age groups are not five years wide, but 1 and 4 years wide respectively
    # since cohort-component projections require equal-sized age intervals, 
    # we'll collapse these into one 5-year interval    
    lt_L_collapsed = lt['L'][2:-1]
    lt_L_collapsed = np.append((lt['L'][0] + lt['L'][1]), lt_L_collapsed)
    
    # survivorship from one age group to next
    lt_L_survivorship = lt_L_collapsed[1:] / lt_L_collapsed[:-1]
    
    # we only need 
    lt_L_survivorship = lt_L_survivorship[:(num_ages-1)]

    # survival for the last (open) age interval
    # (for UNPD life tables, this will be survivorship for 75+)
    # we'll use T80/T75
    lt_L_survivorship_open = np.sum(lt_L_collapsed[-2:])/np.sum(lt_L_collapsed[-3:])
    
    # T85/T80, since the highest age group we'll use is 75-80
    # NOTE: we're collapsing to 80+, instead of 85+, to match the population distributions we have
    lt_L_ratio_open = lt_L_collapsed[-3] / np.sum(lt_L_collapsed[-3:])

    # survivorships go along the subdiagonal of the leslie matrix
    indexes = np.diag_indices_from(leslie_mat)
    subdiag_indexes = (indexes[0][1:], indexes[1][:-1])
    
    leslie_mat[subdiag_indexes] = lt_L_survivorship
    
    # and the bottom-right corner or the survivorship matrix has the open age interval survivorship
    leslie_mat[(-1,-1)] = lt_L_ratio_open
    
    ##############################
    ## calculate net maternity (first row of Leslie matrix)
    ##############################
    
    # approx fraction births that is female (from Wachter)
    fab = 0.4886
    
    # get radix of life table
    radix = lt.sort('age').column('l').item(0)
    
    # get nL0 value from life table
    # (note that this is the sum of the first two entries, which are ages 0-1 and 1-5)
    nL0 = lt_L_collapsed[0]

    # get the indices for the life table L values that correspond to
    # ages with nonzero fertility
    fage_L_idx = np.where(np.isin(lt['age'], asfr['age']))
    # ... and we need L values one beyond the highest fertility age
    # ... this are shifted by -1 because we collapsed the first two age groups
    fage_L_idx = np.arange(start=np.min(fage_L_idx)-1, stop=np.max(fage_L_idx)+1)
    
    # extract the life table L values corresponding to nonzero fertility
    fage_L = lt_L_collapsed[fage_L_idx]

    # survival from one age interval to next corresponding 
    # to ages with nonzero fertility
    fage_surv = fage_L[1:]/fage_L[:-1]
    
    # row-vector of fertilities, with 0s filled in
    fert = np.zeros(shape=(num_ages,))
    
    fert[fage_L_idx[:-1]] = asfr.sort('age').column('asfr')

    ## see formula in, eg, Wachter pg 107 or Preston et al pg 130
    k = fab * (1/2) * (nL0/radix)

    # fertility from younger age group surviving forward and spending half time in new age group
    first_term = np.append(fert[1:] * lt_L_survivorship, 0.0)
    # fertility from older age group before surviving up to next age group
    second_term = fert
    
    A = k * (first_term + second_term)

    # helpful for debugging
    #print('fert:', fert)
    #print('==================================')
    #print('lt_L_survivorship:', lt_L_survivorship)
    #print('==================================')
    #print('first_term: ', first_term)
    #print('==================================')    
    #print('second_term: ', second_term)
    #print('==================================')
    #print('k: ', k)
    #print('==================================')         
    #print('A:', A)
    
    # net maternities along the top row
    leslie_mat[0] = A
    
    return(leslie_mat)

#lmat = make_leslie_matrix('France', 2010)

# helpful for debugging - print a matrix out nicely
#for x in lmat:
#    for y in x:
#        print("%1.3f" % round(y,3), end =" ")
#    print("\n")

def project(pop, leslie_matrix):
    new_pop = np.dot(leslie_matrix, pop)
    return(new_pop)

def get_growth_rate(lmat):
    # dominant eigenvalue of the Leslie matrix, lambda_1, is the factor by which
    # the population grows every 5 years
    # so lambda_1 = exp(5r), where r is the intrinsic growth rate we defined before
    # thus, r = log(lambda_1)/5
    lambda_1 = np.real(np.max(np.linalg.eig(lmat)[0]))    
    return(np.log(lambda_1)/5)

def repeat_project(start_pop, lmat, num_projection_steps=50):
    
    proj_pop = Table().with_columns('iteration', 0,
                                    'size', np.sum(start_pop))
    proj_pop = proj_pop.with_columns(zip([str(a) for a in all_ages], normalize_distn(start_pop)))
    
    n = start_pop

    for i in np.arange(start=1, stop=num_projection_steps):

        n = project(n, lmat)

        current_size = np.sum(n)
        current_n_norm = normalize_distn(n)

        proj_pop = proj_pop.with_row(list(np.append([i,
                                                     current_size],
                                                     current_n_norm)))
    
    return(proj_pop)

def self_project(country, period, num_projection_steps):
    lmat = make_leslie_matrix(country, period)
    start_pop = get_pop_vec(country, period)

    result = repeat_project(start_pop, lmat, num_projection_steps)
    
    return(result)

def compare_projection_agedistn(projection_result):
    start_idx = 0
    final_idx = projection_result.num_rows-1

    start_size = projection_result.column('size').item(start_idx)
    start_age_distn = projection_result.drop(['iteration', 'size']).row(start_idx)
    
    final_size = projection_result.column('size').item(final_idx)
    final_age_distn = projection_result.drop(['iteration', 'size']).row(final_idx)
    
    return(Table().with_columns('age', all_ages,
                                'start', start_age_distn,
                                'end', final_age_distn))
