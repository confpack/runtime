from __future__ import absolute_import

from . import utils

import json
import os
import unittest

from cprt import environment


class TestEnvironment(utils.RunnerTestCase):
  def setUp(self):
    self.memorize_environ()

  def tearDown(self):
    self.restore_environ()

  def test_from_file(self):
    env = environment.Environment.from_file(utils.TEST_CONFIG_PATH, utils.TEST_VARIABLES_PATHS)
    self.assertDictEqual(utils.EXPECTED_TEST_CONFIG, env.config)
    self.assertDictEqual(utils.EXPECTED_TEST_VARIABLES, env.variables)

  def test_from_environment(self):
    os.environ["CONFPACK_VAR_TEST_VAR"] = "123"
    os.environ["CONFPACK_VAR_TEST_COMPLEX"] = json.dumps({"a": [1, 2, 3]})
    os.environ["CONFPACK_CONFIG_TEST_CNF"] = "234"
    os.environ["CONFPACK_CONFIG_TEST_COMPLEX"] = json.dumps({"a": [1, 2, 3]})

    env = environment.Environment.from_environment()
    self.assertEqual(123, env.variables["test_var"])
    self.assertDictEqual({"a": [1, 2, 3]}, env.variables["test_complex"])

    self.assertEqual(234, env.config["test_cnf"])
    self.assertDictEqual({"a": [1, 2, 3]}, env.config["test_complex"])

  @unittest.skipIf(not utils.on_ci() and not utils.on_vagrant(), "discover_system only runs on vagrant or CI")
  def test_discover_system(self):
    pass

  def test_dump_to_environment(self):
    env = environment.Environment.from_file(utils.TEST_CONFIG_PATH, utils.TEST_VARIABLES_PATHS)
    env.dump_to_environment()

    env2 = environment.Environment.from_environment()
    self.assertDictEqual(utils.EXPECTED_TEST_CONFIG, env2.config)
    self.assertDictEqual(utils.EXPECTED_TEST_VARIABLES, env2.variables)
    self.assertEqual("1", os.environ["CONFPACK_USE_ENV"])

  def test_setup_environment(self):
    main = environment.SetupEnvironmentMain()
    argv = utils.TEST_VARIABLES_PATHS[:]
    argv.insert(0, utils.TEST_CONFIG_PATH)
    main(argv)

    env = environment.Environment.from_environment()
    self.assertDictEqual(utils.EXPECTED_TEST_CONFIG, env.config)
    self.assertDictEqual(utils.EXPECTED_TEST_VARIABLES, env.variables)
    self.assertEqual("1", os.environ["CONFPACK_USE_ENV"])

if __name__ == "__main__":
  unittest.main()
