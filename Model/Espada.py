#!/usr/bin/python
#-*- coding: utf-8 -*-

from Objeto import Objeto

class Espada(Objeto):
    def __init__(self):
        self.poder = None

    def ver(self):
        print("Has visto una espada")
