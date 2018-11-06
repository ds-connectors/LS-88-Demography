test = {
  'name': 'High fertility growth rate',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(uganda_high_fert_r, .036712926592991829, rtol=.005)
          True
          """,
          'hidden': False,
        }         
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
