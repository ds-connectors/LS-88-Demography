test = {
  'name': 'Calculate ptr',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(net_migrants.sort('fips').column('ptr').item(3), 0.04246265679712779, rtol=.005)
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
