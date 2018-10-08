test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'Kenya').column('cdr')[0], 10.323)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'Kenya').column('roni')[0], 3.4805999999999999)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_roni_1990.where('area', 'France').column('roni')[0], 0.38499999999999995)
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
