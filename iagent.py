# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:40:56 2016

@author: s1130801031
"""
import random
import operator

class IAgent:     

    def __init__(self):
        pass

    def Update(self, textDict, caves):
        self._coor = (
            int(textDict["currentcave"]["rowN"]),
            int(textDict["currentcave"]["colN"])
            )
        self._arrowsCount = textDict["iagent"]["arrowcount"]
        self._legsCount = textDict["iagent"]["legscount"]
        self._dir = textDict["iagent"]["dir"]
        self._dirsUtility = caves[self._coor[0]][self._coor[1]].GetDirsUtilities(caves)

    def _ChoosePassiveAct(self):
        onRight = {"Up": "onRight", "Down": "onLeft", "Left": "upSideDn", "Right": "noAct"}
        onLeft = {"Up": "onLeft", "Right": "upSideDn", "Down": "onRight", "Left": "noAct"}
        onTop = {"Right": "onLeft", "Down": "upSideDn", "Left": "onRight", "Up": "noAct"}
        onDown = {"Up": "upSideDn", "Right": "onRight", "Left": "onLeft", "Down": "noAct"}        
        chooseDir = {"Right" : onRight, "Left" : onLeft, "Up" : onTop, "Down" : onDown}        
        passiveAct = chooseDir[self._GetMaxKey()][self._dir]
        return passiveAct
    
    def _GetMaxKey(self):
        maxItem = max(self._dirsUtility.items(), key = operator.itemgetter(1))[1]
        maxItems = []
        for i in self._dirsUtility.keys():
            if self._dirsUtility[i] == maxItem:
                maxItems.append(i)
        return maxItems[random.randint(0, len(maxItems) - 1)]

    def ChooseAct(self, caves):
        isGold = caves[self._coor[0]][self._coor[1]].IsGold()
        if isGold:
            return "noAct Take"
        return self._ChoosePassiveAct() + " Go"
