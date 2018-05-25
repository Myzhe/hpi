#!/usr/bin/python
# -*- coding: utf-8 -*-

import thread
import time
from random import randint

def aufnehmen(gabel):
    while (True):
        if (gabeln[gabel]):
            gabeln[gabel] = False;
            break

def abgeben(gabel):
    gabeln[gabel] = True;

def denken(philosoph):
    time.sleep(randint(5, 10))

def essen(philosoph):
    print "\rPhilosoph {:1} isst gerade".format(philosoph + 1)
    time.sleep(randint(5, 10))

def philosoph(name, index):
    while (True):
        denken(index)
        aufnehmen(min(index, (index + 1) % tischGroesse))
        aufnehmen(max(index, (index + 1) % tischGroesse))
        essen(index)
        abgeben(max(index, (index + 1) % tischGroesse))
        abgeben(min(index, (index + 1) % tischGroesse))

tischGroesse = 5
gabeln = [True] * (tischGroesse)

for i in range(tischGroesse):
    thread.start_new_thread(philosoph, ("Mensch", i))

while True:
    pass

