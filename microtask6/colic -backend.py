# imports
from graal.backends.core.colic import CoLic, CATEGORY_COLIC_NOMOS, CATEGORY_COLIC_SCANCODE
from graal.graal import GraalCommand

# setting graal argument parser
parser = GraalCommand.setup_cmd_parser()

arg = ['https://github.com/sumitskj/Prajawalan2019.git',
       '--git-path', '/tmp/clone']

args = parser.parse(*arg)

# nomos exec_path
exec_path = '/home/sumit/fossology/src/nomos/agent/nomossa'

# Colic object initialization
cc = CoLic(uri=args.uri, git_path=args.git_path, exec_path=exec_path)

# fetch all commits
for com in cc.fetch():
    print(com['data']['CommitDate'])