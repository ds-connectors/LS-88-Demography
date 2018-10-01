test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Argentina'))['mac'][0], 28.097)
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Angola'))['tfr'][0], 5.95)
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
