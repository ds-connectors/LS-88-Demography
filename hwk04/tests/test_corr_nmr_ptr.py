test = {
  'name': 'Correlation between ptr and nmr',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(nmr_ptr_corr, 0.17741706693265963, rtol=.005)
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
