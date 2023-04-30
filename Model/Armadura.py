#!/usr/bin/python
#-*- coding: utf-8 -*-

from Objeto import Objeto

class Armadura(Objeto):
    def __init__(self):
        self.vida = None

    def ver(self):
        print("Has visto una armadura")
