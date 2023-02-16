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

