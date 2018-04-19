from __future__ import generators
import plus
import AI
from AI import vector3
import Arenas
import Gooey
import math

class NoBrain(AI.SuperAI):
    "AI that does nothing."
    name = "No Brain"

    def __init__(self, **args):
        AI.SuperAI.__init__(slef, **args)

        self.tactics.append(Tactics.Charge(self))
        self.tactics.append(Tactics.Shove(self))

    def Tick(self):
        # do our stuff here
    
        self.total += self.tickInterval
        if self.total > self.delay:
            self.total = 0

        return AI.SuperAI.Tick(self)

AI.register(NoBrain)
