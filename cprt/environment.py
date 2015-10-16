import argparse
import json
import os

from .helpers import verify_file_exists_or_sysexit


CONFPACK_VAR_PREFIX = "CONFPACK_VAR_"
CONFPACK_CONFIG_PREFIX = "CONFPACK_CONFIG_"
CONFPACK_USE_ENV = "CONFPACK_USE_ENV"

DEFAULT_CONFIG_FILE_PATH = "/etc/confpack/config.json"
DEFAULT_VARIABLE_FILES_PATHS = ["/etc/confpack/variables.json", "/etc/confpack/secrets.json"]


def get_environment(config_file=DEFAULT_CONFIG_FILE_PATH, variables_files=DEFAULT_VARIABLE_FILES_PATHS):
  if os.environ.get(CONFPACK_USE_ENV) == "1":
    return Environment.from_environment()
  else:
    return Environment.from_file(config_file, variables_files)


class Environment(object):
  @classmethod
  def from_environment(cls):
    config = {}
    variables = {}
    for key in os.environ:
      if key.startswith(CONFPACK_VAR_PREFIX):
        varkey = key[len(CONFPACK_VAR_PREFIX):].lower()
        variables[varkey] = json.loads(os.environ[key])
      elif key.startswith(CONFPACK_CONFIG_PREFIX):
        confkey = key[len(CONFPACK_CONFIG_PREFIX):].lower()
        config[confkey] = json.loads(os.environ[key])

    return Environment(config, variables)

  @classmethod
  def from_file(cls, config_file, variables_files):
    with open(config_file) as f:
      config = json.load(f)

    variables = {}
    for fn in variables_files:
      if not os.path.exists(fn):
        continue

      with open(fn) as f:
        variables.update(json.load(f))

    return Environment(config, variables)

  def __init__(self, config, variables):
    self.config = config
    self.variables = self.discover_system_facts()
    self.variables = variables

  def discover_system_facts(self):
    # TODO: not yet implemented.
    return {}

  def dump_to_environment(self):
    for key, value in self.config.iteritems():
      os.environ[CONFPACK_CONFIG_PREFIX + key.upper()] = json.dumps(value)

    for key, value in self.variables.iteritems():
      os.environ[CONFPACK_VAR_PREFIX + key.upper()] = json.dumps(value)

    os.environ[CONFPACK_USE_ENV] = "1"


class SetupEnvironmentMain(object):
  def __init__(self):
    self.argparser = argparse.ArgumentParser(description="Setup the environment for confpack-runtime. Dumps config and variables into the environment for faster runs")
    self.argparser.add_argument("config", nargs="?", default=DEFAULT_CONFIG_FILE_PATH, help="config file path. default: /etc/confpack/config.json")
    self.argparser.add_argument("variables", nargs="*", default=DEFAULT_VARIABLE_FILES_PATHS, help="variable files paths. default: /etc/confpack/variables.json /etc/confpack/secrets.json")
    self.argparser.prog = self.argparser.prog + " setup_environment"

  def get_help(self):
    return self.argparser.format_help()

  def get_description(self):
    return self.argparser.description

  def __call__(self, argv):
    args = self.argparser.parse_args(argv)

    verify_file_exists_or_sysexit(args.config, self.argparser)
    for vfn in args.variables:
      verify_file_exists_or_sysexit(vfn, self.argparser)

    Environment.from_file(args.config, args.variables).dump_to_environment()
