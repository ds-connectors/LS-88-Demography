test = {
  'name': 'Baseline growth rate',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_90_r, 0.033093561575554556, rtol=.005)
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
