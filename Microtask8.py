#imports
import argparse
import os
import shutil
from graal.graal import GraalRepository

# Parse command line arguments
parser = argparse.ArgumentParser(description='Arguments passing')

# adding arguments
parser.add_argument("-u", "--uri", help="repo url")
parser.add_argument("-c", "--hash", help="hash")

args = parser.parse_args()

# repository url
repo_uri = args.uri

# commit SHA
sha = args.hash

# making string - git command to clone
str = 'git clone --mirror '+ repo_uri + ' /tmp/repo'

# removing the repositiories earlier stored in /tmp/repo folder
shutil.rmtree('/tmp/repo')

# Cloning
os.system(str)
print("cloning done")

# path of repository cloned
repo_dir = '/tmp/repo'

# making an GraalRepository obect
obj = GraalRepository(uri=repo_uri, dirpath=repo_dir)

# creating an worktree
obj.worktree(worktreepath='/tmp/worktrees')

# updating worktreepath
obj.worktreepath = '/tmp/worktrees'

# doing a checkout to the given commit SHA
obj.checkout(hash=args.hash)

# Using flake8 to find errors if any
flk = "flake8 "+repo_dir

err = os.system(flk)

if err == 0:
    print("OK")
else:
    print(err)

