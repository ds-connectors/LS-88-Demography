test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> math.isclose(ca_lt_ex['Males'][3], 76.159999999999997)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> math.isclose(ca_lt_ex['Females'][4], 79.75)
          True
          """,
          'hidden': False,
          'locked': True
        },  
        {
          'code': r"""
          >>> ca_lt_ex['Age'][0] == 0
          True
          """,
          'hidden': False,
          'locked': True
        },          
        {
          'code': r"""
          >>> ca_lt_ex['Age'][20] == 20
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
