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
from portunhol import conbertir_frasses_cumplietas


def main(argv):
    if len(argv) == 1:
        print ('Utilizacion: %s'
               ' <nombre de archivo>') % os.path.basename(__file__)
        sys.exit(0)

    punteiro_de_archivo = open(argv[1])
    finalmiente = ''
    for linea in punteiro_de_archivo:
        finalmiente += conbertir_frasses_cumplietas(linea) + '\n'

    print (finalmiente + "\n\nPor supuesto!")

if __name__ == '__main__':
    main(sys.argv)
