from __future__ import absolute_import

import subprocess

from .package_manager_backend import PackageManagerBackend


class AptBackend(PackageManagerBackend):
  def __init__(self):
    pass

  def name(self):
    return "apt"

  def update_cache(self):
    """Updates the local cache of all packages.

    Corresponds to something like apt-get update.
    """
    raise NotImplementedError

  def upgrade(self, *packages):
    """Upgrades a list of packages provided.

    If no packages are provided, upgrade all possible.

    During upgrade, files that exists from previous versions but does
    not existing the current version MUST be removed. Dependencies must be
    autoremoved if they are not longer dependant.
    """
    raise NotImplementedError

  def install(self, *packages):
    """Installs a list of packages provided.

    At least one package must be provided.
    """
    raise NotImplementedError

  def remove(self, *packages):
    """Remove a list of packages provided.

    If none is provided, nothing happens.
    """
    raise NotImplementedError