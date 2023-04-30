#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Hechizo(Decorator):
    def __init__(self):
        self.activa = False
        self.tipoHechizo = None

    def entrar(self):
        if self.activa:
            self.tipoHechizo.entrar()
        else:
            self.component.entrar()

