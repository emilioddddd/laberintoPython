#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

class Main(object):
    """
    def main(self):
       
        juego = Juego()
        juego.EjercicioCompositeDecorator()
        #juego.laberinto2Habitaciones()
        #juego.laberinto2HabitacionesFM()
        #juego.laberinto4HabitacionesFM()
        #juego.laberinto4HabitacionesFMBomba()
        #juego.laberinto4HabitacionesFMBichos()
        for hab in juego.laberinto.habitaciones:
            print(hab)
            hab.entrar()
            hab = self.component(hab)
            self.habitacion(hab)
            print("")
            

        for bichos in juego.bichos:
            self.bich(bichos)
    """
    def component(self, decorado):
        if hasattr(decorado, 'component'):
            return decorado.component
        else:
            return decorado

    def habitacion(self, habitacion):
        print(habitacion)
        print(habitacion.num)
        print(habitacion.norte)
        habitacion.norte.entrar()
        print(habitacion.sur)
        habitacion.sur.entrar()
        print(habitacion.oeste)
        habitacion.oeste.entrar()
        print(habitacion.este)
        habitacion.este.entrar()
        print(habitacion.hijos)
        self.contene(habitacion)

    def bich(self, bicho):
        print(bicho)
        print(bicho.modo)
        print(bicho.vida)
        print(bicho.poder)
        print(bicho.posicion.num)

    def contene(self, cont):
        if hasattr(cont, 'hijos'):
            for h in cont.hijos:
                print(h)
     
                self.contene(h)
       
main = Main()        
juego = Juego()
juego.EjercicioCompositeDecorator()        
#juego.laberinto2Habitaciones()
#juego.laberinto2HabitacionesFM()
#juego.laberinto4HabitacionesFM()
#juego.laberinto4HabitacionesFMBomba()
#juego.laberinto4HabitacionesFMBichos()
for hab in juego.laberinto.habitaciones:
    print(hab)
    hab.entrar()
    hab = main.component(hab)        
    main.habitacion(hab)        
    print("\n ------------------------------------------------------------------------------")
            

for bichos in juego.bichos:
    main.bich(bichos)

