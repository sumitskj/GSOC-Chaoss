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