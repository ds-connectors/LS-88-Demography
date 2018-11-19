from IPython.core.display import HTML
from datascience import *

#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
import numpy as np
import os
#plt.style.use('fivethirtyeight')

import pandas as pd
import zipfile
import io
import math

import folium
import json
import pandas as pd
import folium.colormap as cm

_us_counties = '../data/us-counties.json'
_geo_json_county_data = json.load(open(_us_counties))

_irs_mig = Table.read_table('irs_mig.csv')

def map_counties(table, qty, colormap=None):
    """
    table - the Table. must have a 'fips' column with county-level FIPS codes
    qty - the column in the table to map
    """
    
    df = table.to_df()
    df['fips'] = df['fips'].astype(str)
    
    qty_dict = df.set_index('fips')[qty]
    
    if colormap is None:
        cmin = np.percentile(qty_dict, 10)
        cmax = np.percentile(qty_dict, 90)
        colormap = cm.LinearColormap(['Red', 'Orange', 'Yellow', 'Green'], 
                                   vmin=cmin,
                                   vmax=cmax)\
                    .to_step(n=30)
                #.to_step(n=20,
                #         data=nmr_dict,
                #         method='quantiles')

            
    def get_map_color(id):
        if id not in qty_dict.keys():
            return('#00000000')
        else:
            return colormap(qty_dict[id])

    m = folium.Map(location=[39, -96], 
                   #tiles="Stamen Toner",
                   tiles='cartodbpositron',
                   zoom_start=4)

    # add the legend
    colormap.caption = qty
    m.add_child(colormap)
    
    folium.GeoJson(_geo_json_county_data,
                   style_function=lambda feature: {
                       'fillColor' : get_map_color(feature['id']),
                       'color' : 'black',
                       'weight' : .5,
                       'opacity' : .8,
                       #'line_opacity' : .3,
                   }).add_to(m)
    

    return(m)

def county_destination_dist(fips):
    orig = _irs_mig.where('from_fips', fips)
    orig = orig.relabel(make_array('from_fips',
                                   'y1_state', 'y1_countyname',
                                   'to_fips',
                                  'y2_state', 'y2_countyname',
                                  'n2'),
                        make_array('origin_fips',
                                   'origin_state', 'origin_county',
                                   'dest_fips',
                                   'dest_state', 'dest_county',
                                   'num_out_migrants'))
    
    # select only the relabeled columns, plus also 'mi_to_country' to include in the result
    orig = orig.select(['origin_fips',
                                   'origin_state', 'origin_county',
                                   'dest_fips',
                                   'dest_state', 'dest_county',
                                   'num_out_migrants', 'mi_to_county'])
    
    # sort the result in descending order of the number of out migrants to each county
    orig = orig.sort('num_out_migrants', descending=True)
    return(orig)

def map_out_migrants(fips):
    tab = county_destination_dist(fips)
    sending_fips = tab.column('origin_fips').item(0)
    tot_sent = -1*np.sum(tab['num_out_migrants'])
    tomap = tab.relabel(make_array('dest_fips', 'num_out_migrants'), make_array('fips', 'num')).select('fips', 'num')
    tomap = tomap.with_row([sending_fips, tot_sent])
    
    cmin = np.min(tomap['num'])
    cmax = np.max(tomap['num'])
    colormap = cm.LinearColormap(['Red', 'Green', 'DarkGreen'], 
                                 index=[cmin,0,cmax],
                                 vmin=cmin, vmax=cmax)

    return(map_counties(tomap, 'num', colormap=colormap))


def county_arrivals_dist(fips):
    ## see the `county_destination_dist` function above for inspiration here    
    dest = _irs_mig.where('to_fips', fips)
    dest = dest.relabel(make_array('to_fips',
                                   'y2_state', 'y2_countyname',                                   
                                   'from_fips',
                                   'y1_state', 'y1_countyname',
                                   'n2'),
                        make_array('dest_fips',
                                   'origin_state', 'origin_county',                                   
                                   'origin_fips',
                                   'dest_state', 'dest_county',
                                   'num_in_migrants'))
    dest = dest.select(['dest_fips',
                        'dest_state', 'dest_county',
                        'origin_fips',
                        'origin_state', 'origin_county',                        
                        'num_in_migrants', 'mi_to_county'])
    dest = dest.sort('num_in_migrants', descending=True)    
    return(dest)

def map_in_migrants(fips):
    tab = county_arrivals_dist(fips)
    receiving_fips = tab.column('dest_fips').item(0)
    tot_arrived = np.sum(tab['num_in_migrants'])
    tomap = tab.relabel(make_array('origin_fips', 'num_in_migrants'), 
                        make_array('fips', 'num')).select('fips', 'num')
    tomap['num'] = -1*tomap.column('num')
    tomap = tomap.with_row([receiving_fips, tot_arrived])
    
    cmin = np.min(tomap['num'])
    cmax = np.max(tomap['num'])
    colormap = cm.LinearColormap(['DarkRed', 'red', 'DarkGreen'], 
                                 index=[cmin,0,cmax],
                                 vmin=cmin, vmax=cmax)

    return(map_counties(tomap, 'num', colormap=colormap))

