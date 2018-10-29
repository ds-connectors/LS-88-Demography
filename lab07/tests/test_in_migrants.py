test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> in_migrants.num_rows == 2695
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> in_migrants.where('fips', 17031).column('num_in_migrants').item(0) == 84079
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
