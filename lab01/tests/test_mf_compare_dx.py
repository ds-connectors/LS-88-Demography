test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> ca_compare_dx['Males'][3] == 14
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ca_compare_dx['Females'][33] == 56
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
