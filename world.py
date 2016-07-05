# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:32:02 2016

@author: s1140501081
"""
import cave

class World:
    def __init__(self, dictText):
        self._size = [4, 4]
        self._newCaveOpened = 0
        self._isMonsterAlive = True
        self._isGoldFinded = False
        self._caves = [cave.Cave([i, j]) for i in range(self._size[0]) for j in range(self._size[1])]
        self._currentCaveCoor = None        
       
    def Update(self, dictText):
        self._isMonsterAlive = bool(int(dictText["worldinfo"]["ismonsteralive"]))
        self._isGoldFinded = bool(int(dictText["worldinfo"]["isgoldfinded"]))
        curCaveInfo = dictText["currentcave"]
        coor = (curCaveInfo["nRow"], curCaveInfo["nCol"])
        self._caves[coor[0]][coor[1]].Update(curCaveInfo)
        self._SetChances();  
    
    def _SetChances(self):
        for i in self._caves:
            for j in i:
                j.SetChances()
        
    def IsGoldFinded(self):
        return self._isGoldFinded
        
    def GetCave(self):
        return self._currentCave