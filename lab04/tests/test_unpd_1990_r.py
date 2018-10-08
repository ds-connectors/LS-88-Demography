test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_1990_r.where('area', 'Armenia').column('r')[0], -0.93461013)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_1990_r.where('area', 'Zimbabwe').column('r')[0], 2.5205255025457256)
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
