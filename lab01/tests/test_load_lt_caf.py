test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> ca_f_lt.num_rows == 110
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ca_f_lt['PopName'][0] == 'CA'
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ca_f_lt['Sex'][0] == 'f'
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ca_f_lt['Year'][0] == 2015
          True
          """,
          'hidden': False,
          'locked': True
        }          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
