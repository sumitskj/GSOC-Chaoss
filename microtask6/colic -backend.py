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