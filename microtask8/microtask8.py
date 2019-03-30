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
import argparse
import os
import shutil
from graal.graal import GraalRepository
from graal.backends.core.analyzers.flake8 import Flake8

# Parse command line arguments
parser = argparse.ArgumentParser(description='Arguments passing')

# adding arguments
parser.add_argument("-u", "--uri", help="repo url")
parser.add_argument("-c", "--hash", help="hash")

args = parser.parse_args()

# repository url
repo_uri = args.uri

# path of repository cloned
repo_dir = '/tmp/repo'

# commit SHA
sha = args.hash

print("Cloning stated..")

# making string - git command to clone
str = 'git clone --mirror ' + repo_uri + ' /tmp/repo'

# removing the repositiories earlier stored in /tmp/repo folder
if os.path.isdir('/tmp/repo'):
    shutil.rmtree('/tmp/repo')

# Cloning
os.system(str)

print("cloning done")

# making an GraalRepository obect
obj = GraalRepository(uri=repo_uri, dirpath=repo_dir)

# creating an worktree
obj.worktree(worktreepath='/tmp/worktrees')

# updating worktreepath
obj.worktreepath = '/tmp/worktrees'

# doing a checkout to the given commit SHA
obj.checkout(hash=args.hash)

# Using flake8 to find errors if any

flk_args = {
    'module_path': os.path.join(os.sep, 'tmp', 'repo'),
    'worktree_path': '/tmp/worktrees',
    'details': True
}

# instantiating flake8
flake8 = Flake8()

check = flake8.analyze(**flk_args)

print("flake 8 results: ")

for keys, values in check.items():
    print(keys)
    print(values)