test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(all_mort.where('country', 'Aruba').select('e0_f', 'adultmort_m')[1][0], 0.120311) == True
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(all_mort.where('country', 'Aruba').select('e0_f', 'adultmort_m')[0][0], 77.7563) == True
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
