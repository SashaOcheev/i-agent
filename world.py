# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:32:02 2016

@author: s1140501081
"""
import cave
import iagent
import functools

class World:
    def __init__(self):
        self._costs = {
            "monster" : -100,
            "hole" : -50,
            "gold" : 100,
            "step" : 1,
            "open" : 2,
        }
        self._size = (4, 4)
        self._caveOpened = 0
        self._isMonsterAlive = True
        self._isGoldFinded = False
        self._caves = [[cave.Cave((i, j)) for j in range(self._size[1])] for i in range(self._size[0])]
        self._agent = iagent.IAgent()
       
    def Update(self, dictText):
        self._isMonsterAlive = bool(int(dictText["worldinfo"]["ismonsteralive"]))
        curCaveInfo = dictText["currentcave"]
        self._currentCaveCoor = (int(curCaveInfo["rowN"]), int(curCaveInfo["colN"]))
        self.GetCave().Update(curCaveInfo)
        self._SetUtilities()
        self._agent.Update(dictText, self.GetCave(), self._caves)
        
    def GetAct(self):
        return self._agent.ChooseAct()
    
    def _SetChances(self):
        for i in self._caves:
            for j in i:
                j.SetChances({
                "gold" : 1.0 / self._GetUnopened(),
                "step" : 1.0,
                "open" : int(j.IsVisiable()),
                "monster" : 0#TODO
                "hole" : 0#TODO
                })

    def _GetUnopened(self):
        res = 0;        
        for i in self._caves:
            for j in i:
                res += int(j.IsVisiable())
        return res
                
    
    def _SetUtilities(self):
        self._SetChances()
        for i in self._caves:
            for j in i:
                j.SetUtility(self._costs)
        for i in self._caves:
            for j in i:
                j.SetDirsUtilities(self._caves)
        
    def IsGoldFinded(self):
        return self._isGoldFinded
        
    def GetCave(self):
        coor = self._currentCaveCoor
        return self._caves[coor[0]][coor[1]]
        