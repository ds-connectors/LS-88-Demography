test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_e0.where('area', 'Germany').where('period', 1965).where('sex', 'female').column('e')[0],72.562783999999994)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> unpd_e0.num_rows == 5226
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
