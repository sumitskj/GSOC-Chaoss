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