from __future__ import generators
import plus
import Arenas
import Hazards
import random

def OnBridge(location):
    return location[0] >= -4.5 and location[0] <= 4.5 and location[2] >= -3 and \
        location[2] <= 3 and location[1] > -.5

class BridgeArena(Arenas.SuperArena):
    "Travel across the bridge to reach your opponent, but watch out for the flame hazards in the corners of the arena."
    name = "Bridge of Doom"
    preview = "bridge/bridge_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-12.0, 15.0, 13.0, -16.0)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/bridge/bridge.gmf")
        plus.setBackColor(0,0,0)
        
        fov = .015
        self.AddStaticCamera("Static Cam 1", (-21.7, 12.49, 0), (.4858, 1.558), 65*fov)
        self.AddStaticCamera("Static Cam 2", (0, 29.8, 0), (1.57, 0), 64*fov)
        
        self.AddWatchCamera("Watch Cam 1", (0.185, 4.398, 3.381), (3, 8, 90*fov, 60*fov))
        self.AddWatchCamera("Watch Cam 2", (-11.6, 3.65, -5.43), (8, 25, 70*fov, 35*fov))

    def AddShadowReceivers(self):
        #Shadow Light Sources
        self.SetShadowSource(0.653, 6.894, -0.418)
        
        #Main Arena Shadow Triangles
        self.AddShadowTriangle((12.7,-0.670113,12.7), (12.7,-0.670113,-12.7), (12.7,8.16321,12.7))
        self.AddShadowTriangle((12.7,8.16321,12.7), (12.7,-0.670113,-12.7), (12.7,8.16321,-12.7))
        self.AddShadowTriangle((-12.7,-0.670113,-12.7), (-12.7,-0.670113,12.7), (-12.7,8.16321,-12.7))
        self.AddShadowTriangle((-12.7,8.16321,-12.7), (-12.7,-0.670113,12.7), (-12.7,8.16321,12.7))
        self.AddShadowTriangle((2.81238,-2.18294,-6.04799), (-2.81238,-2.18294,-6.04799), (-2.81238,-0.670435,-10.6348))
        self.AddShadowTriangle((2.81238,-2.18294,-6.04799), (-2.81238,-0.670435,-10.6348), (2.81238,-0.670435,-10.6348))
        self.AddShadowTriangle((-2.81238,-2.18294,6.04799), (2.81238,-2.18294,6.04799), (2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((-2.81238,-2.18294,6.04799), (2.81238,-0.670435,10.6348), (-2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((-12.7,-0.670113,-12.7), (-2.54001,-0.670113,-15.24), (-2.81238,-0.670435,-10.6348))
        self.AddShadowTriangle((2.81238,-0.670435,-10.6348), (-2.81238,-0.670435,-10.6348), (-2.54001,-0.670113,-15.24))
        self.AddShadowTriangle((2.81238,-0.670435,-10.6348), (-2.54001,-0.670113,-15.24), (2.54001,-0.670113,-15.24))
        self.AddShadowTriangle((2.81238,-0.670435,-10.6348), (2.54001,-0.670113,-15.24), (12.7,-0.670113,-12.7))
        self.AddShadowTriangle((2.81238,-0.670435,-10.6348), (12.7,-0.670113,-12.7), (12.7,-0.670113,12.7))
        self.AddShadowTriangle((2.81238,-0.670435,10.6348), (2.81238,-0.670435,-10.6348), (12.7,-0.670113,12.7))
        self.AddShadowTriangle((2.81238,-0.670435,10.6348), (12.7,-0.670113,12.7), (2.54001,-0.670113,15.24))
        self.AddShadowTriangle((-12.7,-0.670113,12.7), (-12.7,-0.670113,-12.7), (-2.81238,-0.670435,-10.6348))
        self.AddShadowTriangle((-12.7,-0.670113,12.7), (-2.81238,-0.670435,-10.6348), (-2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((-2.54001,-0.670113,15.24), (-12.7,-0.670113,12.7), (-2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((2.54001,-0.670113,15.24), (-2.54001,-0.670113,15.24), (-2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((2.81238,-0.670435,10.6348), (2.54001,-0.670113,15.24), (-2.81238,-0.670435,10.6348))
        self.AddShadowTriangle((2.81238,-2.18294,6.04799), (-2.81238,-2.18294,6.04799), (-2.81238,-2.18294,-6.04799))
        self.AddShadowTriangle((2.81238,-2.18294,6.04799), (-2.81238,-2.18294,-6.04799), (2.81238,-2.18294,-6.04799))
        
        #Bridge Shadow Triangles
        self.AddShadowTriangle((3.8324,-0.639962,2.47193), (2.04571,-0.128098,2.47193), (2.04571,-0.128098,-2.52808))
        self.AddShadowTriangle((3.8324,-0.639962,2.47193), (2.04571,-0.128098,-2.52808), (3.8324,-0.639962,-2.52808))
        self.AddShadowTriangle((2.04571,-0.128098,2.47193), (-2.28099,-0.128098,2.47193), (-2.28099,-0.128098,-2.52808))
        self.AddShadowTriangle((2.04571,-0.128098,2.47193), (-2.28099,-0.128098,-2.52808), (2.04571,-0.128098,-2.52808))
        self.AddShadowTriangle((-2.28099,-0.128098,2.47193), (-4.07734,-0.64962,2.47193), (-4.07734,-0.64962,-2.52808))
        self.AddShadowTriangle((-2.28099,-0.128098,2.47193), (-4.07734,-0.64962,-2.52808), (-2.28099,-0.128098,-2.52808))
        
    def HazardsOn(self, on):
        if on:
            self.flame1 = Hazards.Flame((-6.74, 1.6, 12.28), (0, -6, 0), (.2, .4, .2), -.25)
            self.AddHazard(self.flame1)
            self.flame2 = Hazards.Flame((6.72, 1.6, 12.28), (0, -6, 0), (.2, .4, .2), -.25)
            self.AddHazard(self.flame2)
            self.flame3 = Hazards.Flame((6.7, 1.6, -12.24), (0, -6, 0), (.2, .4, .2), -.25)
            self.AddHazard(self.flame3)
            self.flame4 = Hazards.Flame((-6.75, 1.6, -12.24), (0, -6, 0), (.2, .4, .2), -.25)
            self.AddHazard(self.flame4)        

            self.RegisterZone("hazardzone01", 1)
            self.RegisterZone("hazardzone02", 2)
            self.RegisterZone("hazardzone03", 3)
            self.RegisterZone("hazardzone04", 4)
            
            self.AddCollisionLine((-8.5, 14.5), (-8.5, 12.5))
            self.AddCollisionLine((-8.5, 12.5), (-5, 12.5))
            self.AddCollisionLine((-5, 12.5), (-5, 14.5))
            
            self.AddCollisionLine((5, 14.5), (5, 12.5))
            self.AddCollisionLine((5, 12.5), (8.4, 12.5))
            self.AddCollisionLine((8.4, 12.5), (8.4, 14.5))
            
            self.AddCollisionLine((-8.5, -14.6), (-8.5, -12.6))
            self.AddCollisionLine((-8.5, -12.6), (-5, -12.6))
            self.AddCollisionLine((-5, -12.6), (-5, -14.6))
            
            self.AddCollisionLine((5, -14.6), (5, -12.6))
            self.AddCollisionLine((5, -12.6), (8.4, -12.6))
            self.AddCollisionLine((8.4, -12.6), (8.4, -14.6))
        else:
            pass

        # walls
        self.AddCollisionLine((-12.7, 12.7), (-12.7, -12.7))
        self.AddCollisionLine((-12.7, -12.7), (-2.5, -15.2))
        self.AddCollisionLine((-2.5, -15.2), (2.5, -15.2))
        self.AddCollisionLine((2.5, -15.2), (12.7, -12.7))
        self.AddCollisionLine((12.7, -12.7), (12.7, 12.7))
        self.AddCollisionLine((12.7, 12.7), (2.5, 15.2))
        self.AddCollisionLine((2.5, 15.2), (-2.5, 15.2))
        self.AddCollisionLine((-2.5, 15.2), (-12.7, 12.7))
        
        # edges
        self.AddCollisionLine((-2.9, 10.6), (-2.9, -10.6))
        self.AddCollisionLine((2.9, 10.6), (2.9, -10.6))

        self.AddPOV(0, (0, 13.5), (1, 2, 3))
        self.AddPOV(1, (0, -13), (0, 4, 5))
        self.AddPOV(2, (4.5, -12), (0, 6))
        self.AddPOV(3, (-4.5, -12), (0, 7))
        self.AddPOV(4, (4.5, 12), (1, 6))
        self.AddPOV(5, (-4.5, 12), (1, 7))
        self.AddPOV(6, (9.5, 0), (2, 4))
        self.AddPOV(7, (-9.5, 0), (3, 5))
        
        return Arenas.SuperArena.HazardsOn(self, on)
        
    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-26.8033,12.2077,14.7377)
        plus.setCameraRotation(0.351528,2.2434)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/aggression.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Bridge_Enter.wav", "Sounds/announcers/Arena_Bridge_Welcome.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Arena_Bridge_PayToll.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Fire_WatchFlames.wav", "Sounds/announcers/Hazard_Fire_GooseCooked.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-26.8033,12.2077,14.7377), (0.351528,2.2434), 0.675, (19.4831,12.2077,13.807), (0.425733,3.881), 0.675, 0, 9)
        yield 4
        
        #play a generic (or specific) secondary comment
        plus.fadeOutLoop(sounds['crowd'], 8000)
        plus.playSound(sounds['generic'])
        
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((6.91983,7.58627,1.19135), (0.278429,-3.14121), 0.675, (6.91983,7.58627,-4.94869), (0.527259,-3.14081), 0.675, 0, 5)
            yield 5

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-7.83619,4.96176,2.53669), (0.523549,-3.14159), 0.675, (1.1777,4.96176,-2.29792), (0.470045,-1.96602), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((4.22518,1.36116,-0.310427), (0.226477,0.472123), 0.675, (0.96244,1.36116,5.91944), (0.254117,1.49149), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((-3.75155,0.743029,2.24349), (0.223871,-0.766732), 0.675, (-1.72234,0.743029,7.70196), (0.206293,-1.80951), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((13.1737,1.41123,-6.55294), (0.37941,-1.54769), 0.675, (9.32725,1.41123,-1.55862), (0.377573,-2.91305), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0

    def Tick(self):
        # do our stuff here
        if self.bHazardsOn:
            self.flame1.Tick()
            self.flame2.Tick()
            self.flame3.Tick()
            self.flame4.Tick()
        
        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        if id ==1:
            self.flame1.ZoneEvent(direction)
        elif id == 2:
            self.flame2.ZoneEvent(direction)
        elif id == 3:
            self.flame3.ZoneEvent(direction)
        elif id == 4:
            self.flame4.ZoneEvent(direction)
        #temp until flamethrower object exists
        #~ if direction == 1:
            #~ locations = ["(-6.73, 12.25, 1.75)", "(6.73, 12.25, 1.75)", "(6.73, -12.25, 1.75)", "(-6.73, -12.25, 1.75)"]
            #~ print "BURN BABY! Location: " + locations[id]
    
        return True

    def GetPath(self, start, end, ignore_hazards):
        # overridden to deal with crossing the bridge

        # pathfind on bridge
        if OnBridge(end) and OnBridge(start):
            return (self.ToGrid(end), )
        # pathfind off bridge
        elif OnBridge(start):
            if end[0] <= 0:
                path1 = Arenas.SuperArena.GetPath(self, (-6, 0, 0), end, ignore_hazards)
                return path1
            elif end[0] >= 0:
                path1 = Arenas.SuperArena.GetPath(self, (6, 0, 0), end, ignore_hazards)
                return path1
        # pathfind onto bridge
        elif OnBridge(end):
            if start[0] <= 0:
                path1 = Arenas.SuperArena.GetPath(self, start, (-6, 0, 0), ignore_hazards)
                return path1 + (self.ToGrid(end),)
            elif start[0] >= 0:
                path1 = Arenas.SuperArena.GetPath(self, start, (6, 0, 0), ignore_hazards)
                return path1 + (self.ToGrid(end),)

        # pathfind across bridge
        if start[2] >= -6 and start[2] <= 6 and end[2] >= -6 and end[2] <= 6:
            if start[0] <= -4.5 and end[0] >= 4.5:
                # crossing west to east
                path1 = Arenas.SuperArena.GetPath(self, start, (-6, 0, 0), ignore_hazards)
                path2 = Arenas.SuperArena.GetPath(self, (6, 0, 0), end, ignore_hazards)
                return path1 + path2
            elif start[0] >= 4.5 and end[0] <= -4.5:
                # crossing east to west
                path1 = Arenas.SuperArena.GetPath(self, start, (6, 0, 0), ignore_hazards)
                path2 = Arenas.SuperArena.GetPath(self, (-6, 0, 0), end, ignore_hazards)
                return path1 + path2

        return Arenas.SuperArena.GetPath(self, start, end, ignore_hazards)

Arenas.register(BridgeArena)
