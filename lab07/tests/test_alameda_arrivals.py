test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> alameda_arrivals.num_rows == 147
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> alameda_arrivals.where('origin_fips', 6077).column('num_in_migrants').item(0) == 2162
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
