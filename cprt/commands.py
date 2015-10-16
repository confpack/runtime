from __future__ import absolute_import, print_function

from .utilities.template import TemplateMain
from .environment import SetupEnvironmentMain

import sys


def get_class_name(command):
  camelized_command = "".join([w.capitalize() for w in command.split("_")])
  return "{}Main".format(camelized_command)


# This class needs to be here because we use globals to detect all submodules.
class HelpMain(object):
  def __init__(self):
    pass

  def get_description(self):
    return "Displays this help screen. A command can be appended to this."

  def __call__(self, argv):
    if len(argv) == 0:
      utility_commands = [(k[:-4].lower(), globals()[k]) for k in globals() if k.endswith("Main")]
      print("usage: {} command".format(sys.argv[0]))
      print("")
      print("commands:")
      for name, klass in utility_commands:
        print("  {}".format(name))
        print("    {}".format(klass().get_description()))
        print("")
    else:
      command = argv[0]
      cls_name = get_class_name(command)
      if cls_name not in globals():
        print("error: {} is not a valid function".format(command), file=sys.stderr)
        self([])
      else:
        p = globals()[cls_name]()
        print(p.get_help())
