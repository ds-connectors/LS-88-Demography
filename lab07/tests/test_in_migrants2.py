test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> in_migrants.where('fips', 17031).column('pop_2015').item(0) == 5245831
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> in_migrants.where('county_name', 'DeKalb County').where('state', 'IL').column('num_in_migrants').item(0) == 2570
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
