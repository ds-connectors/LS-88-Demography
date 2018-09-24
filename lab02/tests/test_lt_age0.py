test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> lt_m_age0.num_rows == 201
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lt_m_age0.where('area', are.equal_to('France')).column('age')[0] == 0
          True
          """,
          'hidden': False,
          'locked': True
        },          
        {
          'code': r"""
          >>> lt_m_age0.where('area', are.equal_to('France')).column('sex')[0] == 'male'
          True
          """,
          'hidden': False,
          'locked': True
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
