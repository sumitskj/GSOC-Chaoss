# imports
from perceval.backends.core.github import GitHub
from perceval.backends.core.github import GitHubCommand

# setting up GitHub Argument parser
parser = GitHubCommand.setup_cmd_parser()

# making arguments list
arg = ['sumitskj'
       , 'GSOC-Chaoss']
args = parser.parse(*arg)

# making Github object
repo = GitHub(owner=args.owner, repository=args.repository)

# fetching user names
for item in repo.fetch():
    print(item['data']['user']['login'])

