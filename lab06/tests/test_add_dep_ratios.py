test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(india_proj_withdr.where('iteration', 9).column('total_dr').item(0), 79.60620021042531)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(india_proj_withdr.where('iteration', 0).column('child_dr').item(0), 73.41500817335282)
          True
          """,
          'hidden': False,
        },
        {
          'code': r"""
          >>> np.isclose(india_proj_withdr.where('iteration', 8).column('old_dr').item(0), 5.97299451216864)
          True
          """,
          'hidden': False,
        },          
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
