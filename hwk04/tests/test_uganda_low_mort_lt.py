test = {
  'name': 'Uganda 90 leslie matrix',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.all(np.isclose(uganda_90_low_mort.sort('age').column('l'), np.array([ 100000.        ,   90404.77226289,   84020.22998037,   81512.80757699,   80148.28013978,   78597.21928117,   76512.43986196,   73780.81185709,   70778.20669182,   67418.65487262,   64028.97850365,   60586.81967234,   56724.82073579,   52201.82195324,   46391.54729107,   38784.81996299,   29262.78369323,   18933.37636218,    9576.92948656]), rtol=.005))
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