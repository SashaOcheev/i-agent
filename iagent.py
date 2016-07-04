# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:40:56 2016

@author: s1130801031
"""
import random

class IAgent:     

    def __init__(self, textDict, currentCave):
        self._tiktak = 0
        self._aname = textDict["iagent"]["aname"]
        self._actsCostList = textDict["iagent"]["actsCostList"]
        self._WStateUtilities = textDict["iagent"]["WStateUtilities"]
        self._IAStateUtilities = textDict["iagent"]["IAStateUtilities"]
        self._currentCave = currentCave
        self._dirsUtility = self._currentCave.GetUtilities()
        self.Update(textDict, currentCave)
        self._OnRight = {"Up": "onRight", "Down": "onLeft", "Left": "upSideDn", "Right": "noAct"}
        self._OnLeft = {"Up": "onLeft", "Right": "upSideDn", "Down": "onRight", "Left": "noAct"}
        self._OnTop = {"Right": "onLeft", "Down": "upSideDn", "Left": "onRight", "Up": "noAct"}
        self._OnDown = {"Up": "upSideDn", "Right": "onRight", "Left": "onLeft", "Down": "noAct"}

    def Update(self, textDict, currentCave):
        self._arrowsCount = textDict["iagent"]["arrowcount"]
        self._direction = textDict["iagent"]["dir"]
        cavenum = list(map(int, textDict["iagent"]["cavenum"].split("_")))
        self._row = cavenum[0]
        self._col = cavenum[1]
        self._legsCount = textDict["iagent"]["legscount"]
        self._isAgentAlive = bool(int(textDict["iagent"]["isagentalive"]))
        self._haveGold = bool(int(textDict["iagent"]["havegold"]))
        self._currentCave = currentCave
        self._dirsUtility = self._currentCave.GetUtilities()
    
        
    def _ChoosePassiveAct(self):
        sortDirs = sorted(_dirsUtility.items(), key = lambda (k, val): val, reverse = True)
        chosenAct = sortDirs[0][0]
        if chosenAct == "Up":
            passiveAct = self._OnTop[self._direction]
        elif chosenAct == "Right":
            passiveAct = self._OnRight[self._direction]
        elif chosenAct == "Left":
            passiveAct = self._OnLeft[self._direction]
        elif chosenAct == "Down":
            passiveAct = self._OnDown[self._direction]
        return passiveAct


    def ChooseAct(self):
        if self._currentCave.IsGold():
            self._haveGold = True
            return "noAct Take"
        return _ChoosePassiveAct() + " Go"

        
        
    def IsAgentAlive(self):
        return self._isAgentAlive


        
