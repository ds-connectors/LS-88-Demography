test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(india_v2.column('10').item(49), 0.07415015038117734)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(india_v2.column('20').item(3), 0.07883676118184157)
          True
          """,
          'hidden': False,
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
