# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:02:17 2016

@author: s1140501081
"""

class Cave:  
    
    def __init__(self, caveDict):
       self._name= caveDict["cNum"]
       self._row = caveDict["rowN"]
       self._col = caveDict["colN"]
       self._isGold = bool(int(caveDict["isGold"]))
       self._isMonster = bool(int(caveDict["isMonster"]))
       self._isBones = bool(int(caveDict["isBones"]))
       self._isHole = bool(int(caveDict["isHole"]))
       self._isWind = bool(int(caveDict["isWind"]))
       self._isVisiable = False
       self._dirList = caveDict["dirList"].keys()
       self._moveUtilities = {}
       self._shootUtilities = {}              
       
    def GetAllowableDirs(self):
         return self._dirList
    
    def IsGold(self):
        return self._isGold