test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> france_trends.where('period', 1985).column('area').item(0) == 'France'
          True
          """,
          'hidden': False
        },  
        {
          'code': r"""
          >>> np.isclose(france_trends.where('period', 1985).column('tfr').item(0), 1.8653)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(france_trends.where('period', 1985).column('e').item(0), 70.6185979)
          True
          """,
          'hidden': False
        }, 
        {
          'code': r"""
          >>> np.isclose(france_trends.where('period', 1985).column('child_mort').item(0), 0.01000451)
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
