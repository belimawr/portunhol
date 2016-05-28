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


def to_portunhol(word):
    if word == 'é':
        word = 'es'
    if word == 'um':
        word = 'uno'
    if word == 'eu':
        word = 'yo'
    if word == 'o':
        word = 'lo'
    if word == 'a':
        word = 'la'
    if word == 'e':
        word = 'y'
    if word == 'há':
        word = 'hay'
    if word == 'não':
        word = 'no'
    if word == 'ou':
        word = 'o'
    if word == 'no':
        word = 'en lo'
    if word == 'na':
        word = 'en la'
    if word == 'você':
        word == 'usted'
    if word == 'nada':
        word = 'nadie'

    if word.endswith('ção'):
        word = word.replace('ção', 'cion')
    if word.endswith('inho'):
        word = word.replace('inho', 'ito')
    if word.endswith('inha'):
        word = word.replace('inha', 'ita')
    if word.endswith('ém'):
        word = word.replace('ém', 'ien')
    if word.endswith('ou'):
        word = word.replace('ou', 'oy')
    if word.endswith('ola'):
        word = word.replace('ola', 'uela')
    if word.endswith('oda'):
        word = word.replace('oda', 'ueda')
    if word.endswith('são'):
        word = word.replace('são', 'sión')

    if word.find('ça') >= 0:
        word = word.replace('ça', 'sa')
    if word.find('ço') >= 0:
        word = word.replace('ço', 'cio')
    if word.find('nh') >= 0:
        word = word.replace('nh', 'ñ')
    if word.find('lh') >= 0:
        word = word.replace('lh', 'll')
    if word.find('er') >= 0:
        word = word.replace('er', 'ier')
    if word.find('ven') >= 0:
        word = word.replace('ven', 'vien')
    if word.find('qua') >= 0:
        word = word.replace('qua', 'cua')
    if word.find('que') >= 0:
        word = word.replace('que', 'quie')
    if word.endswith('m'):
        word = word.replace('m', 'n')

    return word
