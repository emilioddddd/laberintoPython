#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Hechizo(Decorator):
    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa:
            print("Esta hechizado ")
        else:
            self.component.entrar()

