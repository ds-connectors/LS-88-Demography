test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> len(all_periods) == 66
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> all_periods[0] == 1950
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
