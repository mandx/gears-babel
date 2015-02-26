import os

from gears.environment import Environment
from gears.finders import FileSystemFinder

from gears_babel import Babel6to5Compiler


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

env = Environment(STATIC_DIR)
env.finders.register(FileSystemFinder([ASSETS_DIR]))
env.compilers.register('.jsx', Babel6to5Compiler.as_handler())
env.register_defaults()


if __name__ == '__main__':
    env.save()
