#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    """Este es concreateComplement"""
    def entrar(self):
        print("Te has chocado con la pared")
