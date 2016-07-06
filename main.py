# -*- coding: utf-8 -*-
"""
Spyder Editor

This 
is a temporary script file.
"""

import requests
import json

import world

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
    

gameid = 134
act = "noAct noAct"
currentWorld = world.World()
fileNumber = 0;
req = requests.get(MakeRequest(gameid, act))
#SaveState(req, "state/"+str(fileNumber) + '.txt')    
state = GetState(req)

while ((state["text"])):
    text = state["text"]
    currentWorld.Update(text)
    act = currentWorld.GetAct()
    req = requests.get(MakeRequest(gameid, act))
    #SaveState(req, "state/"+str(fileNumber) + '.txt')    
    state = GetState(req)
    fileNumber += 1

print(fileNumber)