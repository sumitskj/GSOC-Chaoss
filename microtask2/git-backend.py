#imports
from perceval.backends.core.git import Git
from perceval.backends.core.git import GitCommand
from datetime import datetime

#setting up Git Argument parser
parser = GitCommand.setup_cmd_parser()

# making arguments list
arg = ['https://github.com/sumitskj/Prajawalan2019.git',
       '--git-path', '/tmp/clone']
args = parser.parse(*arg)

# making Git object
repo = Git(uri=args.uri, gitpath=args.git_path)

# finding the no. of commits and listing them all
count = 0

from_date = datetime(2018, 10, 12)
to_date = datetime(2019, 12, 9)
branches = 'master'

item = list(repo.fetch(category='commit', from_date=from_date, to_date=to_date))

print("Number of commmits: %d." % len(item))
j=0
for i in item:
    j=j+1
    print("Commit no "+str(j)+": "+ i['data']['commit'])