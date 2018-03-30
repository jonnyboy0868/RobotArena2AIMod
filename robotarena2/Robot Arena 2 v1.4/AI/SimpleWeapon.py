from __future__ import generators
import plus
import AI
from AI import vector3
import Arenas
import Gooey
import math
import Tactics

class SimpleWeapon(AI.SuperAI):
    "Executes its 'Fire!' input every 5 seconds."
	name = "Simple Weapon"

	def __init__(self, **args):
		AI.SuperAI.__init__(self, **args)
		self.zone = "weapon"
		self.triggers = ["Fire"]
		self.reloadTime = 0
		self.reloadDelay = 3
	
		self.tactics.append(Tactics.Engage(self))
	
	

	
	#added by jon to get the bot to ativate 
	def Activate(self, active):
		if active:
		
		self.RegisterSmartZone(self.zone, 1)
		return AI.SuperAI.Activate(self, active)
		
    def Tick(self):
        # do our stuff here
        self.total += self.tickInterval
        if self.total > self.delay:
            #fire piston!
            self.Input("Fire", 0, 1)
            self.total -= self.delay

        return plus.AI.Tick(self)

AI.register(SimpleWeapon)
