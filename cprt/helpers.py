from __future__ import print_function

import os
import sys


def verify_file_exists_or_sysexit(path, argparser=None):
  if not os.path.isfile(path):
    print("error: {} is not a valid file".format(path), file=sys.stderr)
    if argparser:
      argparser.print_help()

    sys.exit(1)
