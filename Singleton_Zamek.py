# -*- coding: utf-8 -*-
u"""Na Zamku powiewa szara flaga. Zamek jest atakowany przez najeźdźców, którzy po zbobyciu Zamku umieszczają swoją flagę. """

def singleton(object, instancje=[]):
    assert object.__class__ not in instancje
    instancje.append(object.__class__)

class Zamek(object):
    def __init__(self):
        singleton(self)

    flaga="SZARA"

    def zmianaFlagi(self, nowaFlaga):
        self.flaga = nowaFlaga

    def wyswietlFlage(self):
        print "Nad zamkien widnieje "+ self.flaga +" flaga."


Wawel = Zamek()


class CzerwoniZdobywcy():
    print "Czerwoni zblizaja sie do zamku."
    Wawel.wyswietlFlage()
    print "Czerwoni atakuja zamek."
    Wawel.zmianaFlagi('CZERWONA')
    print "Zamek zdobyty przez Czerwonych!"
    print "><" * 40


class NiebiescyZdobywcy():
    print "Niebiescy zbliżają się do zamku."
    Wawel.wyswietlFlage()
    print "Niebiescy atakują zamek."
    Wawel.zmianaFlagi("NIEBIESKA")
    print "Zamek zdobyty przez Niebieskich! "
    print "><" * 40

class ZieloniZdobywcy():
    print "Zieloni zbliżają się do zamku."
    Wawel.wyswietlFlage()
    print "Zieloni atakują zamek."
    Wawel.zmianaFlagi("ZIELONA")
    print "Zamek zdobyty przez Zielonych!"
    print "><" * 40

c=CzerwoniZdobywcy()
n=NiebiescyZdobywcy()
z=ZieloniZdobywcy()