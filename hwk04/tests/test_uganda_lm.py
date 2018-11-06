test = {
  'name': 'Uganda 90 leslie matrix',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_90_lm[0][3], 0.52368571638475703, rtol=.005)
          True
          """,
          'hidden': False,
        }, 
        {
          'code': r"""
          >>> np.isclose(uganda_90_lm[3][2], 0.98084361699305356, rtol=.005)
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
