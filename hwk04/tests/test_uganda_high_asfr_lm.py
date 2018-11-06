test = {
  'name': 'Uganda high fertility leslie matrix',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_high_fert_lm[0][3], 0.57605428802323277, rtol=.005)
          True
          """,
          'hidden': False,
        }, 
        {
          'code': r"""
          >>> np.isclose(uganda_high_fert_lm[3][2], 0.98084361699305356, rtol=.005)
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
