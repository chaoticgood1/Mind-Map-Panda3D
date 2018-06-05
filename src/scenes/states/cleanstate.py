from state import State
from stateManager import StateManager

class CleanState(State):
  
  def __init__(self, map):
    State.__init__(self)
    self.map = map
    
  def enter(self):
    map = self.map 
    map.createNodeData(None, "Main")
    self.initEvents()
    
    
  def exit(self):
    print("exit clean state")
    self.map.showBase.ignoreAll()
    
    
  """ enter() helpers """
  def initEvents(self):
    map = self.map
    map.showBase.accept("mouse1", self.mouse1Down)
    
    map.showBase.accept("mouse3", self.mouse3Down)

  def mouse1Down(self):
    selectedNodeData = self.map.getSelectedNodeData()
    if selectedNodeData is None:
      self.switchToScrollingState()
    else:
      self.switchToNodeClickedState(selectedNodeData)
      
      
  def mouse3Down(self):
    selectedNodeData = self.map.getSelectedNodeData()
    if selectedNodeData is None:
      print("None selected")
    else:
      StateManager.switchToEditTextState(self, selectedNodeData)
      
      
  """ mouse3Down Helper """
  
      
      
  def switchToNodeClickedState(self, selectedNodeData):
    print("Switch to node clicked mode")
    
    map = self.map
    self.exit()
    from scenes.states.nodeClickedState import NodeClickedState
    map.state = NodeClickedState(self.map)
    map.state.enter(selectedNodeData)
    
  def switchToScrollingState(self):
    self.map.state.exit()
    
    from scenes.states.scrollingMapState import ScrollingMapState
    self.map.state = ScrollingMapState(self.map)
    self.map.state.enter()
    self.map.state.mouse1Down()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    