# -*- coding: utf-8 -*-
"""
this is the data process module ,
process excel data from temporary directory  to game directory ,
for  Yanteng's game analysis program.
Author : fibonacci
Connect : ericpan1124@yahoo.com
Edit date :20180524
Accomplish : Yes
Final : No
"""
import os


class SplitData:
    def __init__(self, gameDegree, gameRound):
        self.fPath = os.path.abspath('..').replace('\\', '/')
        self.fromPath = self.fPath + "/" + "tmp"
        self.gameRound = gameRound
        self.gameDegree = gameDegree
        self.outPath = self.fPath + "/" + self.gameDegree + "/" +self.gameRound

    def showAll(self):
        print(self.fPath)
        print(self.fromPath)
        print(self.gameRound)
        print(self.gameDegree)
        print(self.outPath)
