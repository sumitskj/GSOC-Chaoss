#imports
import argparse
from perceval.backends.core.github import GitHub

# Parse command line arguments
parser = argparse.ArgumentParser(
    description="Parser for taking arguments"
)


# adding arguments
parser.add_argument("-r", "--repo", help="owner/repo")
parser.add_argument("-t", "--token", help="token")
args = parser.parse_args()

# fetching owner and repo
(owner, repo) = args.repo.split('/')

# making Github object
repo = GitHub(owner=owner, repository=repo, api_token=args.token)

# fetching user names
for item in repo.fetch():
    print(item['data']['user']['login'])

