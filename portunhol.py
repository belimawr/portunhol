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

class paraPortunhol:
    def __init__(self):
        self.portugues = ['é','um','eu','o','a','e','há','não','ou','no','na','você','nada','hoje']
        self.portunhol = ['es','uno','yo','lo','la','y','hay','no','o','en lo','en la','usted','nadie','hoy']

        self.portuguesTerms = ['ção','inho','inha','ém','ou','ola','oda','são','m']
        self.portunholTerms = ['cion','ito','ita','ien','oy','uela','ueda','sión','n']

        self.portuguesTem = ['ça','ço','nh','lh','er','ven','qua','que']
        self.portunholTem = ['sa', 'cio', 'ñ', 'll', 'ier', 'vien', 'cua', 'quie']

    def to_portunhol(self,frase):
        words = frase.split(" ")
        for word in words:
            d = words.index(word)
            words[d] = word.lower()


        for word in words: # para cada palavra nas palavras
            if word in self.portugues: #se a palavra estiver localizada na listagem pt-br
                i = self.portugues.index(word) # pega o indice da palavra no dicionario ptbr
                d = words.index(word)
                words[d] = self.portunhol[i]

        for word in words: # para palavra nas palavras
            for terminacao in self.portuguesTerms:
                if word.endswith(terminacao): #se a palavra termina em TERMINAÇÃO
                    i = self.portuguesTerms.index(terminacao) #pega o indice da terminacao
                    d = words.index(word) #pega o indice da palavra
                    words[d] = words[d].replace(terminacao, self.portunholTerms[i]) #faz o replace


        for word in words: # para palavra nas palavras
            for existe in self.portuguesTem:
                if word.find(existe) >= 0: #se a palavra termina em TERMINAÇÃO
                    try:
                        d = words.index(word)
                        i = self.portuguesTem.index(existe)
                        words[d] = words[d].replace(existe, self.portunholTem[i])
                    except:
                        pass


        fraseFeita  = ""
        for word in words:
            fraseFeita = fraseFeita + " " + word
        return fraseFeita

    def traduz(self, frase):
        traduzida = paraPortunhol.to_portunhol(frase)
        fraseCompleta = ""
        for palavra in traduzida:
            fraseCompleta = fraseCompleta + " " + palavra
