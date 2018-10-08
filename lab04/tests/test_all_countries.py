test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> len(all_countries) == 233
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> all_countries[0] == 'Afghanistan'
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
