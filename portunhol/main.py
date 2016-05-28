# -*- coding: utf-8 -*-
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import sys
from portunhol import to_portunhol


def main(argv):
    if len(argv) == 1:
        print 'Usage %s <filename>' % os.path.basename(__file__)
        sys.exit(0)

    fp = open(argv[1])

    i = 0
    final = ''
    for line in fp:
        i += 1
        for word in line.strip().split(' '):
            word = word.lower()
            final += to_portunhol(word) + ' '
        final += '\n'

    print final

if __name__ == '__main__':
    main(sys.argv)
