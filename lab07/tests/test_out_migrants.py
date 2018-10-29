test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> out_migrants.num_rows == 2671
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> out_migrants.where('fips', 17031).column('num_out_migrants').item(0) == 114872
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
