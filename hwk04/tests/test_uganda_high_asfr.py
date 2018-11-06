test = {
  'name': 'Uganda 90 leslie matrix',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.all(np.isclose(uganda_90_high_asfr.sort('age').column('asfr'), np.array([ 0.2039972,  0.3492632,  0.3422342,  0.2911568,  0.2338314,0.1026234,  0.0388938]), rtol=.005))
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
