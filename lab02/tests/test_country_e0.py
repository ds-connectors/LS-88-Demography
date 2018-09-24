test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> e0_2015.num_rows == 201
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> np.isclose(e0_2015.where('country', are.equal_to('Aruba'))['e0_m'][0], 72.858401)
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
