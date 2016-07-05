# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:40:56 2016

@author: s1130801031
"""
import random
import operator

class IAgent:     

    def __init__(self, textDict):
        self._tiktak = 0
        self._costs = {
            "monster" : -100,
            "hole" : -50,
            "gold" : 100,
            "step" : 1,
            "open" : 2,
        }
        self._aname = textDict["iagent"]["aname"]

    def Update(self, textDict, currentCave):
        self._arrowsCount = textDict["iagent"]["arrowcount"]
        self._direction = textDict["iagent"]["dir"]
        self._legsCount = textDict["iagent"]["legscount"]
        self._currentCave = currentCave
        self._dirsUtility = self._currentCave.GetDirsUtilities()

    def _ChoosePassiveAct(self):
        onRight = {"Up": "onRight", "Down": "onLeft", "Left": "upSideDn", "Right": "noAct"}
        onLeft = {"Up": "onLeft", "Right": "upSideDn", "Down": "onRight", "Left": "noAct"}
        onTop = {"Right": "onLeft", "Down": "upSideDn", "Left": "onRight", "Up": "noAct"}
        onDown = {"Up": "upSideDn", "Right": "onRight", "Left": "onLeft", "Down": "noAct"}        
        changeDir = {onRight, onLeft, onTop, onDown}        
        passiveAct = changeDir[self._GetMaxKey()][self._direction]
        return passiveAct
    
    def _GetMaxKey(self):
        maxItem = max(self._dirsUtility.items(), key = operator.itemgetter(1))[1]
        maxItems = []
        for i in self._dirsUtility.keys():
            if self._dirsUtility[i] == maxItem:
                maxItems.append(i)
        return maxItems[random.randint(0, len(maxItems))]

    def ChooseAct(self):
        if self._currentCave.IsGold():
            return "noAct Take"
        return self._ChoosePassiveAct() + " Go"
