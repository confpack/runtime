
class PackageManagerBackend(object):
  def __init__(self):
    pass

  def name(self):
    """Returns the name of the backend.

    For example, if the backend is apt, it should return "apt", and so forth.
    """
    raise NotImplementedError

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

