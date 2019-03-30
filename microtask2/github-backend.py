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

