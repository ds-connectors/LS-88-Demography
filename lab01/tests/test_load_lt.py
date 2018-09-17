test = {
  'name': 'load life table',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> test_lt.num_rows == 110
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> test_lt['PopName'][0] == 'NY'
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> test_lt['Sex'][0] == 'm'
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> test_lt['Year'][0] == 2015
          True
          """,
          'hidden': False,
        }          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
