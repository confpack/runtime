# All tests should import this module because we set the path here.
# This module should be the first thing imported by tests!

import getpass
import os.path
import unittest
import sys

TEST_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_DATADIR_PATH = os.path.join(TEST_DIR_PATH, "testdata")

VENDOR_DIR = os.path.join(os.path.dirname(TEST_DIR_PATH), "vendor")
sys.path.append(VENDOR_DIR)

TEST_CONFIG_PATH = os.path.join(TEST_DATADIR_PATH, "config.json")
TEST_VARIABLES_PATHS = [
  os.path.join(TEST_DATADIR_PATH, "variables.json"),
  os.path.join(TEST_DATADIR_PATH, "secrets.json"),
]

TEST_TEMPLATE_PATH = os.path.join(TEST_DATADIR_PATH, "nginx.conf.j2")

EXPECTED_TEST_CONFIG = {
  "option1": "1",
  "option2": ["1", "2"],
}

EXPECTED_TEST_VARIABLES = {
  "abc": 456,  # overwritten in secrets.json as it is second.
  "bcd": ["1", "2", "3"],
  "secret1": "abcdef",
}


def on_ci():
  return getpass.getuser() == "travis"


def on_vagrant():
  return getpass.getuser() == "vagrant"


class RunnerTestCase(unittest.TestCase):
  def memorize_environ(self):
    self.old_environ = dict(os.environ)

  def restore_environ(self):
    os.environ.clear()
    os.environ.update(self.old_environ)
