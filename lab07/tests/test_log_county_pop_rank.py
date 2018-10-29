test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(county_pop_rank.where('pop_rank', 100).column('minus_log_rank').item(0), -4.60517)
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
