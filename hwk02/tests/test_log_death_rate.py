test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': r"""
          >>> np.isclose(unpd_2015.where('area', 'France').where('age', 10).where('sex', 'female')['log_death_rate'][0], -9.41797973675) == True
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
