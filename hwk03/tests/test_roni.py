test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_roni.where('area', 'Malawi').where('period', 2000).column('roni').item(0), 28.261)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni.where('area', 'Germany').where('period', 1960).column('roni').item(0), 5.069)
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
