test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(np.round(np.min(swe_5q0.column('child_mort')), 6), 0.0025530)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(np.round(np.max(swe_5q0.column('child_mort')), 6), 0.020552)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.min(swe_5q0.column('period')) == 1955
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.max(swe_5q0.column('period')) == 2015
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
