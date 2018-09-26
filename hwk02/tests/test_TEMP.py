test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> len(all_periods) == 13
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> all_periods[0] == 1955
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> all_periods[12] == 2015
          True
          """,
          'hidden': False,
          'locked': True
        },                 
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
