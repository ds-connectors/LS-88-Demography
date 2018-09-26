test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> index_for_age_15 == 4
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> index_for_age_60 == 13
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
