test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> ca.num_rows == 7
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> ca.where('origin_fips', 1117).column('num_in_migrants').item(0) == 50
          True
          """,
          'hidden': False,
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
