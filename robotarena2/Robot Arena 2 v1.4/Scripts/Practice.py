import plus
import Arenas
import Gooey

class PracticeArena(Arenas.SuperArena):
    "Practice Arena."
    name = "Practice Arena"
    preview = "practice arena/practice_preview.bmp"
    in_list = False

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/practice arena/practice_arena.gmf")
        self.window = None

    def AddShadowReceivers(self):
        #Shadow Light Sources
        self.SetShadowSource(0.653, 6.894, -0.418)
        
        #Arena Shadow Faces
        self.AddShadowTriangle((-6.7561,0.0170998,17.1496), (-6.7561,0.0170998,-5.58268), (6.27657,0.0170998,17.1496))
        self.AddShadowTriangle((6.27657,0.0170998,-5.58268), (6.27657,0.0170998,17.1496), (-6.7561,0.0170998,-5.58268))
        self.AddShadowTriangle((6.27657,0.0170998,-5.58268), (-6.7561,0.0170998,-5.58268), (6.27657,6.94643,-5.58268))
        self.AddShadowTriangle((-6.7561,6.94643,-5.58268), (6.27657,6.94643,-5.58268), (-6.7561,0.0170998,-5.58268))
        self.AddShadowTriangle((-6.7561,0.0170998,17.1496), (6.27657,0.0170998,17.1496), (-6.7561,6.94643,17.1496))
        self.AddShadowTriangle((6.27657,6.94643,17.1496), (-6.7561,6.94643,17.1496), (6.27657,0.0170998,17.1496))
        self.AddShadowTriangle((-6.7561,0.0170998,-5.58268), (-6.7561,0.0170998,17.1496), (-6.7561,6.94643,-5.58268))
        self.AddShadowTriangle((-6.7561,6.94643,17.1496), (-6.7561,6.94643,-5.58268), (-6.7561,0.0170998,17.1496))
        
    def Tick(self):
        # do our stuff here
        return plus.Arena.Tick(self)
        
    def setObstacle(self, name):
        self.RemoveXtra("Obstacle")
        
        if name == "none cb":
            self.window = None
        elif name == "crates cb":
            self.AddXtraSound("Obstacle", "arenas\\crates\\crates.gmf", "metal", "Sounds\\crate.wav")
        elif name == "blocks cb":
            self.AddXtraSound("Obstacle", "arenas\\cinderblocks\\blocks.gmf", "metal", "Sounds\\cinderblock2.wav")
        elif name == "barrels cb":
            self.AddXtraSound("Obstacle", "arenas\\barrels\\barrels.gmf", "metal", "Sounds\\barrel_collision2.wav")
        elif name == "cones cb":
            self.AddXtraSound("Obstacle", "arenas\\cones\\cones.gmf", "metal", "Sounds\\cone.wav")
        elif name == "ramps cb":
            self.AddXtra("Obstacle", "arenas\\ramps\\ramps.gmf", "metal")

Arenas.register(PracticeArena)
