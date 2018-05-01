from direct.showbase.ShowBase import ShowBase

from scenes.map import Map

import json

import os.path as path

 
class Epiphany(ShowBase):
 
  def __init__(self):
    ShowBase.__init__(self)
    self.loadJson(self.initMap)

  def loadJson(self, onLoadJsonFn):
    jsonPath =  path.abspath(path.join(__file__ ,"../../assets/start.json"))
    jsonData = json.load(open(jsonPath))
    onLoadJsonFn(jsonData)


  def initMap(self, jsonData):
    map = Map(self, jsonData)


 
app = Epiphany()
app.run()