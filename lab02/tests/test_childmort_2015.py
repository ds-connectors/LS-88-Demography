test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> childmort_2015.num_rows == 201
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(childmort_2015.where('country', are.equal_to('Denmark'))['childmort_m'][0],0.00429676)
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(childmort_2015.where('country', are.equal_to('Denmark'))['childmort_f'][0],0.0038797999999999888)
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
