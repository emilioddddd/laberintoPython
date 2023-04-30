#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = None
        self.hijos = []

    def ponerEnElemento(self, unaOrientacion, unEM):
        unaOrientacion.ponerElementoEn(unEM, self)

    def entrar(self):
        pass

    
    def agregarHijo(self, unEM):
        unEM.padre = self
        self.hijos.append(unEM)
    
    




