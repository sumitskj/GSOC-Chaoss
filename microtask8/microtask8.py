# Copyright (C) 2019  Sumit Kumar Jangir

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author:
#      Sumit Kumar Jangir <sumitjangirdss.1@gmail.com>

# imports

import os
import shutil
from graal.graal import GraalRepository, GraalCommand
from graal.backends.core.analyzers.flake8 import Flake8

# setting graal argument parser
parser = GraalCommand.setup_cmd_parser()

arg = ['https://github.com/sumitskj/GSOC-Chaoss.git']

args = parser.parse(*arg)


# repository url
repo_uri = args.uri

# commit SHA
sha = '9230281aa93a593939f9dfff4a207f9e8140cb4f'

# worktree directory path
worktreepath = '/tmp/worktrees'

# path of repository cloned
repo_dir = '/tmp/repo'

print("Cloning stated..")

# Cloning the repo if it is not present
if not GraalRepository.exists(repo_dir):
    repo = GraalRepository.clone(repo_uri, repo_dir)
elif os.path.isdir(repo_dir):
    repo = GraalRepository(repo_uri, repo_dir)

# creating a new worktree if not already present
if GraalRepository.exists(worktreepath):
    shutil.rmtree(worktreepath)

repo.worktree(worktreepath)

# preforming checkout at given SHA
repo.checkout(sha)

print("cloning done")


# Using flake8 to find errors if any

flk_args = {
    'module_path': os.path.join(os.sep, 'tmp', 'fossology'),
    'worktree_path': '/tmp/worktrees',
    'details': True
}

# instantiating flake8
flake8 = Flake8()

check = flake8.analyze(**flk_args)

print("flake 8 results: ")

for val in check['lines']:
    print('type:'+val['type_of_warning']+ '  line:'+ val['line']+ '  column:'+ val['column']+ '  desc:'+ val['description'])

