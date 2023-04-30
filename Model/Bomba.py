#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    """
    Bomba es y tiene el elemnto,
    ahora no hace falta habitacionBomba ni paredBomba porque
    """
    def __init__(self):
        self.activa = False
        self.poder = None
        self.tipoBomba = None

    def entrar(self):
        if self.activa == True:
            self.tipoBomba.entrar()
            self.activa = False
        else:
            self.component.entrar()

