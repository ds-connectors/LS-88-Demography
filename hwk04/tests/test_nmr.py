test = {
  'name': 'Calculate nmr',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(net_migrants.sort('fips').column('nmr').item(3), 0.0013297282921856301, rtol=.005)
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
