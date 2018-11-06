test = {
  'name': 'Low mortality growth rate',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_low_mort_r, 0.034288990578645963, rtol=.005)
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
