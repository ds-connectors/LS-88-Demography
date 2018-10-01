test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Austria'))['pctf_primary'][0], 48.5654)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Azerbaijan'))['gdp'][0], 7496.29)
          True
          """,
          'hidden': False
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
