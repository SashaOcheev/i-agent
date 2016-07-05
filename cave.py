# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:02:17 2016

@author: s1140501081
"""

class Cave:  
    
    def __init__(self, coor):
        self._coor = coor
        self._isVisiable = False
        self._chances = { "monster" : 1.0 / 16.0, "hole" : 1.0 / 15.0, "gold" : 1.0 / 16.0, "step" : 1.0, "open" : 1.0}
    
    def Update(self, caveDict):
        self._isVisiable = True
        self._isGold = bool(int(caveDict["isGold"]))
        self._isMonster = bool(int(caveDict["isMonster"]))
        self._isHole = bool(int(caveDict["isHole"]))
        self._isBones = bool(int(caveDict["isBones"]))
        self._isWind = bool(int(caveDict["isWind"]))
        self._dirList = caveDict["dirList"].keys()
    
    def IsVisiable(self):
        return self._isVisiable
    
    def GetAllowableDirs(self):
        return self._dirList
    
    def IsGold(self):
        return self._isGold
        
    def SetChances(self):
        
            
    def GetChances(self):
        return self._chances
    
    def GetCoor(self):
        return coor
        