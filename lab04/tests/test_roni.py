test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'Kenya').column('cdr')[0], 17.503)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'Kenya').column('roni')[0], 2.7625999999999999)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'France').column('roni')[0], -0.39360000000000001)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'France').column('cbr')[0], 13.567)
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
