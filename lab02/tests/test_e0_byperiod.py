test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> e0_byperiod.num_rows == 5226
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> e0_byperiod.labels == ('area', 'sex', 'period', 'e')
          True
          """,
          'hidden': False,
          'locked': True
        },   
        {
          'code': r"""
          >>> np.isclose(e0_byperiod.where('sex', are.equal_to('male')).where('area', are.equal_to('Malawi')).where('period', are.equal_to(1955))['e'][0],35.799978)
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
