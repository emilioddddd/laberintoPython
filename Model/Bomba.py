#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    """
    Bomba es y tiene el elemnto,
    ahora no hace falta habitacionBomba ni paredBomba porque
    """
    def __init__(self):
        self.activa = None

    def entrar(self):
        if self.activa == True:
            print("La bomba ha explotado")
            self.activa = False
        
        return super().entrar()

