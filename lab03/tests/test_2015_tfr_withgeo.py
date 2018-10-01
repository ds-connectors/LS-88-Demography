test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> unpd_tfr_2015.where('area', are.equal_to('Austria'))['subregion_name'][0] == 'Western Europe'
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> unpd_tfr_2015.where('area', are.equal_to('Algeria'))['income_level'][0] == 'middle'
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
