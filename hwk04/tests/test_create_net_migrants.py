test = {
  'name': 'Create net_migrants',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(net_migrants.where('fips', 1017).column('omr').item(0), 0.02832077249175695, rtol=.005)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(net_migrants.where('fips', 1017).column('imr').item(0), 0.027113754121526144, rtol=.005)
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
