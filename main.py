# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pprint
import requests
import json
import os

import world
import iagent

def MakeRequest(gameid, act):
    head = 'http://mooped.net/local/its?module=game&action=agentaction&gameid=' + str(gameid) + '&act='
    return head + act
 
def SaveState(req, name):
    f = open(name, 'w')
    f.write(req.text)
    f.close()
   
def GetState(req):
    json_string = str(req.text)
    return json.loads(json_string)

gameid = 29
act = "noAct noAct"
req = requests.get(MakeRequest(gameid, act))
state = GetState(req)
currentWorld = world.World(state["text"])
agent = iagent.IAgent(state["text"], currentWorld.GetCave())

fileNumber = 1;
while ((state["text"])):
    req = requests.get(MakeRequest(gameid, act))
    SaveState(req, "state/"+str(fileNumber) + '.txt')    
    state = GetState(req)
    text = state["text"]
    currentWorld.Update(text)
    agent.Update(text, currentWorld.GetCave())
    act = agent.ChooseAct()
    fileNumber += 1