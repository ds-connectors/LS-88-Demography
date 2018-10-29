test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> cd.num_rows == 6
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> cd.where('dest_fips', 1073).column('num_out_migrants').item(0) == 47
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
