from __future__ import absolute_import

from .. import utils

import os
import tempfile

from cprt.utilities import template


class TestTemplateMain(utils.RunnerTestCase):
  @classmethod
  def setUpClass(cls):
    with open(utils.TEST_TEMPLATE_PATH) as f:
      cls._test_template = f.read()

  def setUp(self):
    self.memorize_environ()

    fd, self.template_path = tempfile.mkstemp()
    f = os.fdopen(fd, "w")
    f.write(self.__class__._test_template)
    f.close()
    os.environ["CONFPACK_USE_ENV"] = "1"

  def tearDown(self):
    os.remove(self.template_path)

    self.restore_environ()

  def test_render_template(self):
    os.environ["CONFPACK_VAR_NGINX_DEFAULT_RETURN_CODE"] = '"400"'
    main = template.TemplateMain()
    main([self.template_path, self.template_path])

    with open(self.template_path) as f:
      content = f.read()

    self.assertEqual("server {\n  listen 80 default_server;\n  server_name _;\n  return 400;\n}", content)
