import getpass
import os.path

TEST_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
TEST_CONFIG_PATH = os.path.join(TEST_DIR_PATH, "testdata", "config.json")
TEST_VARIABLES_PATHS = [
  os.path.join(TEST_DIR_PATH, "testdata", "variables.json"),
  os.path.join(TEST_DIR_PATH, "testdata", "secrets.json"),
]

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
