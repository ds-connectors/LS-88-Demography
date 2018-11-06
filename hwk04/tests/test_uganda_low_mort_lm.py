test = {
  'name': 'Uganda low mortality leslie matrix',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_low_mort_lm[0][3], 0.53194150491690328, rtol=.005)
          True
          """,
          'hidden': False,
        }, 
        {
          'code': r"""
          >>> np.isclose(uganda_low_mort_lm[3][2], 0.98274151405462606, rtol=.005)
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
