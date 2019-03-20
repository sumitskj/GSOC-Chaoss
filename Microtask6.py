#! /usr/bin/env python3
import argparse
from graal.backends.core.cocom import CoCom

# Parse command line arguments
parser = argparse.ArgumentParser(description='Arguments passing')

# adding arguments
parser.add_argument("-u", "--uri", help="repo url")

args = parser.parse_args()


# URL for the git repo to analyze
repo_uri = args.uri

# directory where to mirror the repo
repo_dir = '/tmp/graal-cocom'

# Cocom object initialization
cc = CoCom(uri=repo_uri, git_path=repo_dir)

# fetch all commits
for com in cc.fetch():
    print(com['data']['CommitDate'])
