from __future__ import generators
import plus
import AI
from AI import vector3
import Arenas
import Gooey
import math
import Tactics

class JonsBot(AI.SuperAI):
    "Switches weapons when one breaks!"
    name = "JonsBot"

    def __init__(self, **args):
        AI.SuperAI.__init__(self, **args)
               
        self.zone1 = "PrimaryWep"
        self.triggers1 = ["PrimaryWep"]
        self.zone2 = "SecondaryWep"
        self.triggers2 = ["SecondaryWep"]
        self.zone3 = "OtherWep"
        self.spin_range = 3.0
        
        if 'range' in args:
            self.spin_range = args.get('range')

        if 'zone' in args: self.zone = args['zone']
        
        if 'triggers' in args: self.triggers1 = args['triggers']
        if 'triggers' in args: self.triggers2 = args['triggers']
        if 'triggers' in args: self.triggers3 = args['triggers']
 	
        self.tactics.append(Tactics.Engage(self))
        
    def Activate(self, active):
        if active:
            if AI.SuperAI.debugging:
                self.debug = Gooey.Plain("watch", 0, 75, 100, 75)
                tbox = self.debug.addText("line0", 0, 0, 100, 15)
                tbox.setText("Throttle")
                tbox = self.debug.addText("line1", 0, 15, 100, 15)
                tbox.setText("Turning")
                tbox = self.debug.addText("line2", 0, 30, 100, 15)
                tbox.setText("")
                tbox = self.debug.addText("line3", 0, 45, 100, 15)
                tbox.setText("")
            
            self.RegisterSmartZone(self.zone1, 1)
            self.RegisterSmartZone(self.zone2, 2)

            
        return AI.SuperAI.Activate(self, active)

    def Tick(self):
        # spin up depending on enemy's range
        enemy, range = self.GetNearestEnemy()
            
        if enemy is not None and range < self.spin_range:
            self.Input("Spin", 0, 1)
        elif self.GetInputStatus("Spin", 0) != 0:
            self.Input("Spin", 0, 0)

        # fire weapon

        targets = [x for x in self.sensors.itervalues() if x.contacts > 0 \
                and not plus.isDefeated(x.robot)]
                       
        bReturn = AI.SuperAI.Tick(self)
        
        return bReturn

    def InvertHandler(self):
        # fire all weapons once per second (until we're upright!)
        while 1:
            for trigger in self.triggers5:
                self.Input(trigger, 0, 1)
            
            for i in range(0, 8):
                yield 0
                
    def LostComponent(self, id):
        # if we lose all our weapons, stop using the Engage tactic and switch to Shove
        if id in self.weapons: self.weapons.remove(id)
        if id in self.sweapons: self.sweapons.remove(id)

        if not self.weapons and not self.sweapons:
            tactic = [x for x in self.tactics if x.name == "Engage"]
            if len(tactic) > 0:
                self.tactics.remove(tactic[0])
                
                self.tactics.append(Tactics.Shove(self))
                self.tactics.append(Tactics.Charge(self))
            
        return AI.SuperAI.LostComponent(self, id)
                
    def DebugString(self, id, string):
        if self.debug:
            if id == 0: self.debug.get("line0").setText(string)
            elif id == 1: self.debug.get("line1").setText(string)
            elif id == 2: self.debug.get("line2").setText(string)
            elif id == 3: self.debug.get("line3").setText(string)

    def SmartZoneEvent(self, direction, id, robot, chassis):
        if id == 1 and self.weapons:
            if robot > 0:
                if direction == 1:
                    for trigger in self.triggers1: self.Input(trigger, 0, 1)
        elif id == 2 and self.sweapons and not self.weapons:
            if robot > 0:
                if direction == 1:
                    for trigger in self.triggers2: self.Input(trigger, 0, 1)
        return True
    
AI.register(JonsBot)
