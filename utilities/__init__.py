from __future__ import absolute_import

import sys

from .templates import TemplateMain

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
      p = globals()["{}Main".format(argv[0].capitalize())]()
      print(p.get_help())
