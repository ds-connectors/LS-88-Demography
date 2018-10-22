test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(us_all_dr.where('period', 1990).column('old_dr').item(0), 22.79315196501489)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(us_all_dr.where('period', 1970).column('child_dr').item(0), 44.02131059598877)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(us_all_dr.where('period', 1955).column('total_dr').item(0), 61.25062886091597)
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
