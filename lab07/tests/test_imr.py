test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(in_migrants.where('fips', 1017).column('imr').item(0), 0.027113754121526144)
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
