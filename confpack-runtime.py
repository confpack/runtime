#!/usr/bin/env python
from __future__ import print_function

import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, "vendor")

sys.path.append(vendor_dir)

import cprt
from cpcommon.cmdline import Cmdline

SCRIPT_NAMES = {"confpack-runtime", "confpack-python", "confpack-runtime.py"}


def main(argv):
  cmdline = Cmdline(SCRIPT_NAMES)
  cmdline.register_command(cprt.SetupEnvironmentMain)
  cmdline.register_command(cprt.TemplateMain)
  return cmdline.main(argv)


if __name__ == "__main__":
  sys.exit(main(sys.argv[:]))
