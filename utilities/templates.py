import argparse
import sys

import jinja2


class TemplateMain(object):
  def __init__(self):
    self.argparser = argparse.ArgumentParser(description="Processes a template file and replaces it all values filled out.")
    self.argparser.add_argument("template", help="The path to the template file. This file is used as the first template file.")
    self.argparser.add_argument("path", help="The path to the result file. This file will be replaced if already exist.")
    self.argparser.add_argument("vars", nargs="*", help="key1=value1 key2=value2 to be executed in the template.")
    self.argparser.prog = self.argparser.prog + " template"

  def get_help(self):
    return self.argparser.format_help()

  def get_description(self):
    return self.argparser.description

  def __call__(self, argv):
    args = self.argparser.parse_args(argv)
    # TODO: verify the path exists via argparser validator.
    self._template = args.template
    self._path = args.path
    self._vars = dict(map(lambda x: x.split("="), args.vars))
    with open(self._template) as f:
      content = f.read()
      template = jinja2.Template(content)
      content = template.render(**self._vars)

    with open(self._path, "w") as f:
      f.write(content)

    return 0

