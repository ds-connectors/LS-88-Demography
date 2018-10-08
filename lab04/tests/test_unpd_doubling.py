test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_1990_r.where('area', 'Armenia').column('Tdbl')[0], -73.827575864831658)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(unpd_1990_r.where('area', 'Zimbabwe').column('Tdbl')[0], 27.375243745921289)
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
