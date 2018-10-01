test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(canmex['Canada'][3],107.51600000000001)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(canmex['Mexico'][2],127.53)
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
