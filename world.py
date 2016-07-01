# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:32:02 2016

@author: s1140501081
"""
import cave

class World:
    def __init__(self, dictText):
        self._newCaveOpened = 0
        self._isMonsterAlive = True
        self._isGoldFinded = False
        self._caves = {}
        self._currentCave = None
             
    def Update(self, dictText):
        self._currentCave = cave.Cave(dictText["currentcave"])
        self._isMonsterAlive = bool(int(dictText["worldinfo"]["ismonsteralive"]))
        self._isGoldFinded = bool(int(dictText["worldinfo"]["isgoldfinded"]))
        
    def IsGoldFinded(self):
        return self._isGoldFinded
        
    def GetCave(self):
        return self._currentCave