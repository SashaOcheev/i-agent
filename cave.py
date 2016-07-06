# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:02:17 2016

@author: s1140501081
"""

class Cave:  
    
    def __init__(self, coor):
        self._coor = coor
        self._isVisiable = False
        self._dirList = []
        self._chances = {}
    
    def Update(self, caveDict):
        self._isVisiable = True
        self._isGold = bool(int(caveDict["isGold"]))
        self._isMonster = bool(int(caveDict["isMonster"]))
        self._isHole = bool(int(caveDict["isHole"]))
        self._isBones = bool(int(caveDict["isBones"]))
        self._isWind = bool(int(caveDict["isWind"]))
        self._dirList = caveDict["dirList"].keys()    
  
    def SetChances(self, chances):
        for key in chances.keys():
            self._chances[key] = chances[key]
        
    #установить полезность текущей пещеры
    def SetUtility(self, costs):
        res = 0;
        for key in costs.keys():
            res += costs[key] * self._chances[key]
        self._utility = res
    
    #взять полезности по допустимым направлениям
    def SetDirsUtilities(self, caves):
        coors = self._GetNeihborsCoor()
        getUtil = lambda key: caves[coors[key][0]][coors[key][1]].GetUtility()
        self._dirsUtilities = {key: getUtil(key) for key in coors}
    
    #словарь Направление : (координаты)
    def _GetNeihborsCoor(self):
        shifts = {
            "Up": (-1, 0),
            "Right": (0, 1),
            "Down": (1, 0),
            "Left": (0, -1)
        }
        makeCoor = lambda key: (
            self.GetCoor()[0] + shifts[key][0],
            self.GetCoor()[1] + shifts[key][1]
        )
        return {key: makeCoor(key) for key in self._dirList}
    
    def _GetUnvisiableNeighborsCount(self, caves):
        count = 0
        coors = self._GetNeihborsCoor().values()
        for coor in coors:
            count += int(not(caves[coor[0]][coor[1]].IsVisiable()))
        return count
    
    def SetNeighborsMonsterChances(self, caves):
        if not(self.IsVisiable()):
            return
        if not(self._isBones):
            return
        count = self._GetUnvisiableNeighborsCount(caves)        
        if not(count):
            return
        chance = 1.0 / float(count)
        coors = self._GetNeihborsCoor().values()
        for coor in coors:
            if not(caves[coor[0]][coor[1]].IsVisiable()):
                caves[coor[0]][coor[1]].AddToMonsterChance(chance)

    def AddToMonsterChance(self, chance):
        self._chances["monster"] += chance
    
    def GetDirsUtilities(self, caves):
        return self._dirsUtilities
    
    def GetUtility(self):
        return self._utility
    
    def GetCoor(self):
        return self._coor
        
    def GetChances(self):
        return self._chances
    
    def IsVisiable(self):
        return self._isVisiable
    
    def IsGold(self):
        return self._isGold