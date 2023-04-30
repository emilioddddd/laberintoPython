#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

class Main(object):
    def main(self):
        juego = Juego()
        #juego.EjercicioCompositeDecorator()
        #juego.laberinto2Habitaciones()
        #juego.laberinto2HabitacionesFM()
        #juego.laberinto4HabitacionesFM()
        #juego.laberinto4HabitacionesFMBomba()
        juego.laberinto4HabitacionesFMBichos()
        for hab in juego.laberinto.habitaciones:
            hab = self.component(hab)
            self.habitacion(hab)
            

        for bichos in juego.bichos:
            self.bich(bichos)

    def component(self, decorado):
        if hasattr(decorado, 'component'):
            return decorado.component
        else:
            return decorado

    def habitacion(self, habitacion):
        print('\n',habitacion)
        print(habitacion.num)
        print(habitacion.hijos)
        print(habitacion.norte)
        habitacion.norte.entrar()
        print(habitacion.sur)
        habitacion.sur.entrar()
        print(habitacion.oeste)
        habitacion.oeste.entrar()
        print(habitacion.este)
        habitacion.este.entrar()

    def bich(self, bicho):
        print(bicho)
        print(bicho.modo)
        print(bicho.vida)
        print(bicho.poder)
        print(bicho.posicion.num)
        

mai = Main()
mai.main()

