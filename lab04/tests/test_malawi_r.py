test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(np.min(country_r['r']),0.2683012127931062)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(np.max(country_r['r']),6.2869285616472936)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(country_r.where('period', 1980).column('r')[0],2.9097781948165324)
          True
          """,
          'hidden': False,
          'locked': True
        },                 
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
