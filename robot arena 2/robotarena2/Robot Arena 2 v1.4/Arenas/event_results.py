import plus
import Arenas

class EventResults(Arenas.SuperArena):
    "Event Result spot."
    name = "Event Results"
    preview = "event_results/nopreview.bmp"
    game_types = ['DEATHMATCH']
    in_list = False

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/event_results/event_results.gmf")
        self.total = 0
        plus.setBackColor(0,0,0)
        
        self.AddStaticCamera("fixed cam", (0, 3.95, -11.88), (0.206, 0), 45*.015)

    def Tick(self):
        # do our stuff here
        self.total += .5
        if self.total > 3.5:
            #print "Skull seconds"
            self.total -= 3.5

        return Arenas.SuperArena.Tick(self)

Arenas.register(EventResults)
