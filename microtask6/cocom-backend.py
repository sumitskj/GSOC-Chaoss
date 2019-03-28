#! /usr/bin/env python3
from graal.backends.core.cocom import CoCom
from graal.graal import GraalCommand

# setting graal argument parser
parser = GraalCommand.setup_cmd_parser()

arg = ['https://github.com/sumitskj/Prajawalan2019.git',
       '--git-path', '/tmp/graal-cocom']

args = parser.parse(*arg)

# Cocom object initialization
cc = CoCom(uri=args.uri, git_path=args.git_path)

# fetch all commits
for com in cc.fetch():
    print(com['data']['CommitDate'])