test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.all(ug_roni.column('area') == 'Uganda')
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.min(ug_roni.column('period')) == 1955
          True
          """,
          'hidden': False
        },          
        {
          'code': r"""
          >>> np.max(ug_roni.column('period')) == 2015
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
