#!/usr/bin/python
#-*- coding: utf-8 -*-

from subprocess import HIGH_PRIORITY_CLASS
from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Bomba import Bomba
from Bicho import Bicho
from Modo import Modo
from Agresivo import Agresivo
from Perezoso import Perezoso
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Armario import Armario

class Juego:
    def __init__(self):
        self.laberinto=None
        self.bichos = []

    def fabriacarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num = unNum
        hab.ponerEnElemento((self.fabricarNorte()), (self.fabricarPared()))
        hab.ponerEnElemento((self.fabricarSur()), (self.fabricarPared()))
        hab.ponerEnElemento((self.fabricarOeste()), (self.fabricarPared()))
        hab.ponerEnElemento((self.fabricarEste()), (self.fabricarPared()))
        hab.hijos = []
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuertaLado1Lado2(self, hab1, hab2):
        puerta = Puerta()
        puerta.lado1=hab1
        puerta.lado2=hab2
        return puerta

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarBomba(self):
        return Bomba()

    def fabricarModoPerzoso(self):
        return Perezoso()

    def fabricarModoAgresivo(self):
        return Agresivo()

    def fabricarBichoAgresivoPosicion(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo
        bicho.vida = 10
        bicho.poder = 10
        bicho.posicion = unaHab
        return bicho

    def fabricarBichoPerezosoPosicion(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerzoso
        bicho.vida = 10
        bicho.poder = 10
        bicho.posicion = unaHab
        return bicho

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarOeste(self):
        return Oeste()

    def fabricarEste(self):
        return Este()

    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def fabricarArmario(self, unCont):
        arm = Armario()

        arm.ponerEnElemento((self.fabricarNorte()), (self.fabricarPared()))
        arm.ponerEnElemento((self.fabricarSur()), (self.fabricarPared()))
        arm.ponerEnElemento((self.fabricarOeste()), (self.fabricarPared()))
        arm.ponerEnElemento((self.fabricarEste()), (self.fabricarPared()))

        unCont.agregarHijo(arm)

    def laberinto2Habitaciones(self):
        self.laberinto=Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta=Puerta()
        puerta.lado1=hab1
        puerta.lado2=hab2

        hab1.norte=Pared()
        hab1.este = Pared()
        hab1.oeste=Pared()

        hab2.sur=Pared()
        hab2.este = Pared()
        hab2.oeste=Pared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2HabitacionesFM(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)

        puerta=self.fabricarPuertaLado1Lado2(hab1, hab2)

        hab1.norte = self.fabricarPared()
        hab1.este = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.sur = puerta

        hab2.sur = self.fabricarPared()
        hab2.este = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto4HabitacionesFM(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)
        hab3 = self.fabriacarHabitacion(3)
        hab4 = self.fabriacarHabitacion(4)

        prt1=self.fabricarPuertaLado1Lado2(hab1, hab2)
        prt2=self.fabricarPuertaLado1Lado2(hab1, hab3)
        prt3=self.fabricarPuertaLado1Lado2(hab3, hab4)
        prt4=self.fabricarPuertaLado1Lado2(hab4, hab2)

        hab1.norte = self.fabricarPared()
        hab1.este = prt2
        hab1.oeste = self.fabricarPared()
        hab1.sur = prt1

        hab2.sur = self.fabricarPared()
        hab2.este = prt4
        hab2.oeste = self.fabricarPared()
        hab2.norte = prt1

        hab3.sur = prt3
        hab3.este = self.fabricarPared()
        hab3.oeste = prt2
        hab3.norte = self.fabricarPared()

        hab4.sur = self.fabricarPared()
        hab4.este = self.fabricarPared()
        hab4.oeste = prt4
        hab4.norte = prt3

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

    def laberinto4HabitacionesFMBomba(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)
        hab3 = self.fabriacarHabitacion(3)
        hab4 = self.fabriacarHabitacion(4)

        prt1=self.fabricarPuertaLado1Lado2(hab1, hab2)
        prt2=self.fabricarPuertaLado1Lado2(hab1, hab3)
        prt3=self.fabricarPuertaLado1Lado2(hab3, hab4)
        prt4=self.fabricarPuertaLado1Lado2(hab4, hab2)

        bm1 = self.fabricarBomba()
        bm2 = self.fabricarBomba()

        hab1.norte = self.fabricarPared()
        hab1.este = prt2
        hab1.oeste = self.fabricarPared()
        hab1.sur = prt1

        bm1.component = self.fabricarPared() 
        hab2.sur = bm1
        #hab2.sur = self.fabricarPared() 
        hab2.este = prt4
        hab2.oeste = self.fabricarPared()
        hab2.norte = prt1

        hab3.sur = prt3
        hab3.este = self.fabricarPared()
        hab3.oeste = prt2
        hab3.norte = self.fabricarPared()

        bm2.component = self.fabricarPared()
        hab4.sur = bm2
        #hab4.sur = self.fabricarPared()
        hab4.este = self.fabricarPared()
        hab4.oeste = prt4
        hab4.norte = prt3

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

    def laberinto4HabitacionesFMBichos(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)
        hab3 = self.fabriacarHabitacion(3)
        hab4 = self.fabriacarHabitacion(4)

        prt1=self.fabricarPuertaLado1Lado2(hab1, hab2)
        prt2=self.fabricarPuertaLado1Lado2(hab1, hab3)
        prt3=self.fabricarPuertaLado1Lado2(hab3, hab4)
        prt4=self.fabricarPuertaLado1Lado2(hab4, hab2)

        hab1.norte = self.fabricarPared()
        hab1.este = prt2
        hab1.oeste = self.fabricarPared()
        hab1.sur = prt1
 
        hab2.sur = self.fabricarPared()
        #hab2.sur = self.fabricarPared() 
        hab2.este = prt4
        hab2.oeste = self.fabricarPared()
        hab2.norte = prt1

        hab3.sur = prt3
        hab3.este = self.fabricarPared()
        hab3.oeste = prt2
        hab3.norte = self.fabricarPared()

        hab4.sur = self.fabricarPared()
        #hab4.sur = self.fabricarPared()
        hab4.este = self.fabricarPared()
        hab4.oeste = prt4
        hab4.norte = prt3

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        self.agregarBicho(self.fabricarBichoAgresivoPosicion(hab1))
        self.agregarBicho(self.fabricarBichoAgresivoPosicion(hab3))
        self.agregarBicho(self.fabricarBichoPerezosoPosicion(hab2))
        self.agregarBicho(self.fabricarBichoPerezosoPosicion(hab4))

    def laberinto4HabitacionesArmarios(self):
        self.laberinto= self.fabricarLaberinto()

        hab1 = self.fabriacarHabitacion(1)
        hab2 = self.fabriacarHabitacion(2)
        hab3 = self.fabriacarHabitacion(3)
        hab4 = self.fabriacarHabitacion(4)

        self.fabricarArmario(hab1)
        self.fabricarArmario(hab2)
        self.fabricarArmario(hab3)
        self.fabricarArmario(hab4)

        prt1=self.fabricarPuertaLado1Lado2(hab1, hab2)
        prt2=self.fabricarPuertaLado1Lado2(hab1, hab3)
        prt3=self.fabricarPuertaLado1Lado2(hab3, hab4)
        prt4=self.fabricarPuertaLado1Lado2(hab4, hab2)
        
        n = self.fabricarNorte()
        s = self.fabricarSur()
        e = self.fabricarEste()
        o = self.fabricarOeste()

        hab1.ponerEnElemento(s, prt1)
        hab1.ponerEnElemento(e, prt2)
        hab2.ponerEnElemento(n, prt1)
        hab2.ponerEnElemento(e, prt4)
        hab3.ponerEnElemento(o, prt2) 
        hab3.ponerEnElemento(s, prt3) 
        hab4.ponerEnElemento(o, prt4) 
        hab4.ponerEnElemento(n, prt4)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)



juego = Juego()
juego.laberinto4HabitacionesArmarios()
print(dir(juego.laberinto.habitaciones[0]))
print(juego.laberinto.habitaciones[0].hijos)
for hab in juego.laberinto.habitaciones:
    print(hab.norte)
    hab.norte.entrar()
    print(hab.sur)
    print(hab.oeste)
    print(hab.este)
    print(hab.num)
    print(hab.hijos)

for bichos in juego.bichos:
    print(bichos.modo)
    print(bichos.posicion.num)
