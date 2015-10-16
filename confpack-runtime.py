#!/usr/bin/env python
from __future__ import print_function

import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, "vendor")

sys.path.append(vendor_dir)

import cprt
import cprt.commands

SCRIPT_NAMES = {"confpack-runtime", "confpack-python", "confpack-runtime.py"}


def main(argv):
  if argv[0] in SCRIPT_NAMES:
    argv.pop(0)

  if len(argv) == 0:
    argv.append("help")  # lol

  command = argv.pop(0)
  cls_name = cprt.commands.get_class_name(command)
  if cls_name in dir(cprt.commands):
    p = getattr(cprt.commands, cls_name, None)()
  else:
    p = cprt.commands.HelpMain()
    argv.insert(0, command)
    p(argv)
    sys.exit(1)

  return p(argv) or 0


if __name__ == "__main__":
  sys.exit(main(sys.argv[:]))
