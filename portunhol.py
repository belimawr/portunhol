#!/bin/env python
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

words = {
    'é': 'es',
    'um': 'uno',
    'uma': 'una',
    'eu': 'yo',
    'o': 'lo',
    'a': 'la',
    'e': 'y',
    'há': 'hay',
    'não': 'no',
    'ou': 'o',
    'no': 'en lo',
    'na': 'en la',
    'da': 'de la',
    'do': 'del',
    'você': 'usted',
    'nada': 'nadie'
}

end_words = {
    'ção': 'cion',
    'ções': 'ciones',
    'ino': 'ito',
    'inha': 'ita',
    'ém': 'ien',
    'ou': 'oy',
    'ola': 'uela',
    'oda': 'ueda',
    'são': 'sión',
    'm': 'n',
    'mento': 'miento'
}

inside_words = {
    'ça': 'sa',
    'ço': 'cio',
    'nh': 'ñ',
    'lh': 'll',
    'er': 'ier',
    'ven': 'vien',
    'qua': 'cua',
    'que': 'quie'
}


def to_portunhol(word):
    for key in words:
        if word == key:
            word = words[key]
    for key in end_words:
        if word.endswith(key):
            word = word.replace(key, end_words[key])
    for key in inside_words:
        if word.find(key) >= 0:
            word = word.replace(key, inside_words[key])
    return word

if len(sys.argv) == 1:
    print ('Usage %s <filename>' % os.path.basename(__file__))
    sys.exit(0)

fp = open(sys.argv[1])

i = 0
final = ''
for line in fp:
    i += 1
    # print 'Linha ' + str(i)
    for word in line.strip().split(' '):
        word = word.lower()
        final += to_portunhol(word) + ' '
        # print '%s ' % to_portunhol(word)
    final += '\n'

print (final)
