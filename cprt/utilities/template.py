from __future__ import absolute_import

import argparse

import jinja2

from .. import environment
from cpcommon import verify_file_exists_or_sysexit, Command


class TemplateMain(Command):
  def __init__(self):
    self.argparser = argparse.ArgumentParser(description="Processes a template file and replaces it all values filled out.")
    self.argparser.add_argument("template", help="The path to the template file. This file is used as the first template file.")
    self.argparser.add_argument("path", help="The path to the result file. This file will be replaced if already exist.")
    self.argparser.prog = self.argparser.prog + " template"

  def get_help(self):
    return self.argparser.format_help()

  def get_description(self):
    return self.argparser.description

  def __call__(self, argv):
    args = self.argparser.parse_args(argv)

    verify_file_exists_or_sysexit(args.template, self.argparser)

    with open(args.template) as f:
      content = f.read()

    template = jinja2.Template(content)
    env = environment.get_environment()
    content = template.render(**env.variables)

    with open(args.path, "w") as f:
      f.write(content)

    return 0
