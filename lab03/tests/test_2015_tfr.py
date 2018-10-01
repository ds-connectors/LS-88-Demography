test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> unpd_tfr_2015.where('area', are.equal_to('Mayotte'))['tfr'][0] == 4.1
          True
          """,
          'hidden': False
        },
        {
          'code': r"""
          >>> unpd_tfr_2015.where('area', are.equal_to('Malawi'))['period'][0] == 2015
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
