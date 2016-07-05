# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:02:17 2016

@author: s1140501081
"""

class Cave:  
    
    def __init__(self, coor):
        self._coor = coor
        self._isVisiable = False
        self._chances = {
            "monster" : 1.0 / 15.0,
            "hole" : 2.0 / 15.0,
            "gold" : 1.0 / 15.0,
            "step" : 1.0,
            "open" : 1.0,
            }
        self._utility = None
        self._dirsUtilities = None
    
    def Update(self, caveDict):
        self._isVisiable = True
        self._isGold = bool(int(caveDict["isGold"]))
        self._isMonster = bool(int(caveDict["isMonster"]))
        self._isHole = bool(int(caveDict["isHole"]))
        self._isBones = bool(int(caveDict["isBones"]))
        self._isWind = bool(int(caveDict["isWind"]))
        self._dirList = caveDict["dirList"].keys()
        
    def _SetChances(self):
        pass
    
    #установить полезность текущей пещеры
    def SetUtility(self, costs):
        res = 0;
        for key in costs.keys():
            res += costs[key] * self._chances[key]
        self._utility = res
    
    #установить полезности по допустимым направлениям
    def SetDirsUtilities(self, caves):
        coors = self._GetNeihborsCoor()
        getUtil = lambda key: caves[coors[key][0]][coors[key][1]].GetUtility()
        self._dirsUtilities = {key: getUtil(key) for key in coors}
    
    #словарь Направление : (координаты)
    def _GetNeihborsCoor(self, caves):
        shifts = {
            "Up": (-1, 0),
            "Right": (0, 1),
            "Down": (-1, 0),
            "Left": (0, -1)
        }
        makeCoor = lambda key: (
            self._dirList[key][0] + shifts[key][0],
            self._dirList[key][1] + shifts[key][1]
        )
        return {key: makeCoor(key) for key in self._dirList}
    
    def GetDirsUtilities(self, caves):
        return self._dirsUtilities
    
    def GetUtility(self):
        return self._utility
        
    def GetChances(self):
        return self._chances
    
    def GetCoor(self):
        return self._coor
    
    def IsVisiable(self):
        return self._isVisiable
    
    def IsGold(self):
        return self._isGold