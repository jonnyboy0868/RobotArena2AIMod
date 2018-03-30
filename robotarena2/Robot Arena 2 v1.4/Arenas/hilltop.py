from __future__ import generators
import plus
import Arenas
import Hazards
import random
from king import KingOfHill

def SideOf(location, m, b): # takes a point, slope, and z-intercept, returns which side of the line (defined
                                      # by the slope and intercept) the point is on
    diff = location[2] - (m * location[0] + b)
    if diff < 0:
        return -1
    elif diff == 0:
        return 0
    else:
        return 1

def InHazard(location):
    if location[0] >= 2.4 and location[2] >= 2.4:
        i = SideOf(location, -1, 11.8)
        if i <= 0:
            return 1
    elif location[0] >= 2.4 and location[2] <=-2.4:
        i = SideOf(location, 1, -11.8)
        if i >= 0:
            return 2
    elif location[0] <= -2.4 and location[2] <=-2.4:
        i = SideOf(location, -1, -11.8)
        if i >= 0:
            return 3
    elif location[0] <=-2.4 and location[2] >= 2.4:
        i = SideOf(location, 1, 11.8)
        if i <= 0:
            return 4
    else:
        return 0
            
class HilltopArena(KingOfHill):
    "Can you be the King of this Hill?"
    name = "Hill Top Arena"
    preview = "hilltop/koth2_preview.bmp"
    game_types = ['KING OF THE HILL']
    extent = (-15.0, 15.0, 16.0, -16.0)

    def __init__(self):
        KingOfHill.__init__(self, "Arenas/hilltop/hilltop.gmf", "King_Zone", 1, (0, 2, 0))
        
        # Static Cameras
        self.AddStaticCamera("Overhead", (0, 47, 0), (1.5708, 3.1415), 0.675)
        self.AddStaticCamera("Side", (-15, 31.7, -15), (0.9198, 0.7875), 0.675)
        
        # Watch Camera
        self.AddWatchCamera("Side", (-2.2, 17.9, -14.7), (5, 10, 0.375, 0.675))

        self.SetMapHazardHeight(-17)
        
    def __del__(self):
        KingOfHill.__del__(self)
        
    def AddShadowReceivers(self):
        self.SetShadowSource(0.017, 24.225, -0.066)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((-2.38,1.78619,-2.38), (2.38,1.78619,-2.38), (2.38,1.78619,2.38))
        self.AddShadowTriangle((2.38,1.78619,2.38), (-2.38,1.78619,2.38), (-2.38,1.78619,-2.38))
        self.AddShadowTriangle((2.38,1.78619,-2.38), (-2.38,1.78619,-2.38), (-2.38,0.0861887,-9.53402))
        self.AddShadowTriangle((-2.38,0.0861887,-9.53402), (2.38,0.0861887,-9.53402), (2.38,1.78619,-2.38))
        self.AddShadowTriangle((-2.38,1.78619,2.38), (2.38,1.78619,2.38), (2.38,0.0861887,9.36402))
        self.AddShadowTriangle((2.38,0.0861887,9.36402), (-2.38,0.0861887,9.36402), (-2.38,1.78619,2.38))
        self.AddShadowTriangle((2.38,1.78619,2.38), (2.38,1.78619,-2.38), (9.36967,0.0861887,-2.38))
        self.AddShadowTriangle((9.36967,0.0861887,-2.38), (9.36967,0.0861887,2.38), (2.38,1.78619,2.38))
        self.AddShadowTriangle((-2.38,1.78619,-2.38), (-2.38,1.78619,2.38), (-9.36967,0.0861887,2.38))
        self.AddShadowTriangle((-9.36967,0.0861887,2.38), (-9.36967,0.0861887,-2.38), (-2.38,1.78619,-2.38))
        self.AddShadowTriangle((2.38,0.0861887,-9.53402), (-2.38,0.0861887,-9.53402), (-2.38,0.0861887,-15.2915))
        self.AddShadowTriangle((-2.38,0.0861887,-15.2915), (9.36967,0.0861887,-15.2915), (2.38,0.0861887,-9.53402))
        self.AddShadowTriangle((-9.36967,0.0861887,-2.38), (-9.36967,0.0861887,2.38), (-15.2972,0.0861887,-2.38))
        self.AddShadowTriangle((-2.38,0.0861887,9.36402), (2.38,0.0861887,9.36402), (2.38,0.0861887,15.2915))
        self.AddShadowTriangle((9.36967,0.0861887,2.38), (9.36967,0.0861887,-2.38), (15.2972,0.0861887,2.38))
        self.AddShadowTriangle((15.2972,0.0861887,2.38), (2.38,0.0861887,15.2915), (2.38,0.0861887,9.36402))
        self.AddShadowTriangle((2.38,0.0861887,9.36402), (9.36967,0.0861887,2.38), (15.2972,0.0861887,2.38))
        self.AddShadowTriangle((-2.38,0.0861887,9.36402), (-9.36967,0.0861887,15.2915), (-9.36967,0.0861887,2.38))
        self.AddShadowTriangle((-9.36967,0.0861887,15.2915), (-2.38,0.0861887,9.36402), (2.38,0.0861887,15.2915))
        self.AddShadowTriangle((-9.36967,0.0861887,-2.38), (-15.2972,0.0861887,-2.38), (-2.38,0.0861887,-15.2915))
        self.AddShadowTriangle((-2.38,0.0861887,-15.2915), (-2.38,0.0861887,-9.53402), (-9.36967,0.0861887,-2.38))
        self.AddShadowTriangle((9.36967,0.0861887,-15.2915), (15.2972,0.0861887,-9.53402), (9.36967,0.0861887,-2.38))
        self.AddShadowTriangle((9.36967,0.0861887,-2.38), (2.38,0.0861887,-9.53402), (9.36967,0.0861887,-15.2915))
        self.AddShadowTriangle((-2.38,0.0861887,-2.38), (-9.36967,0.0861887,-2.38), (-2.38,0.0861887,-9.53402))
        self.AddShadowTriangle((2.38,0.0861887,2.38), (9.36967,0.0861887,2.38), (2.38,0.0861887,9.36402))
        self.AddShadowTriangle((9.36967,0.0861887,-15.2915), (-2.38,0.0861887,-15.2915), (-2.38,2.39342,-15.2915))
        self.AddShadowTriangle((-2.38,2.39342,-15.2915), (9.36967,2.39342,-15.2915), (9.36967,0.0861887,-15.2915))
        self.AddShadowTriangle((2.38,0.0861887,15.2915), (15.2972,0.0861887,2.38), (15.2972,2.39342,2.38))
        self.AddShadowTriangle((15.2972,2.39342,2.38), (2.38,2.39342,15.2915), (2.38,0.0861887,15.2915))
        self.AddShadowTriangle((-2.38,0.0861887,-15.2915), (-15.2972,0.0861887,-2.38), (-15.2972,2.39342,-2.38))
        self.AddShadowTriangle((-15.2972,2.39342,-2.38), (-2.38,2.39342,-15.2915), (-2.38,0.0861887,-15.2915))
        self.AddShadowTriangle((2.38,0.0861887,-2.38), (2.38,0.0861887,-9.53402), (9.36967,0.0861887,-2.38))
        self.AddShadowTriangle((-2.38,0.0861887,2.38), (-2.38,0.0861887,9.36402), (-9.36967,0.0861887,2.38))
        self.AddShadowTriangle((9.36967,0.0861887,-2.38), (15.2972,0.0861887,-9.53402), (15.2972,0.0861887,2.38))
        self.AddShadowTriangle((15.2972,2.39342,2.38), (15.2972,0.0861887,2.38), (15.2972,0.0861887,-9.53402))
        self.AddShadowTriangle((15.2972,0.0861887,-9.53402), (15.2972,2.39342,-9.53403), (15.2972,2.39342,2.38))
        self.AddShadowTriangle((15.2972,2.39342,-9.53403), (15.2972,0.0861887,-9.53402), (9.36967,0.0861887,-15.2915))
        self.AddShadowTriangle((15.2972,2.39342,-9.53403), (9.36967,0.0861887,-15.2915), (9.36967,2.39342,-15.2915))
        self.AddShadowTriangle((-15.2972,0.0861887,9.36402), (-9.36967,0.0861887,2.38), (-9.36967,0.0861887,15.2915))
        self.AddShadowTriangle((-9.36967,0.0861887,2.38), (-15.2972,0.0861887,9.36402), (-15.2972,0.0861887,-2.38))
        self.AddShadowTriangle((-15.2972,2.39342,-2.38), (-15.2972,0.0861887,-2.38), (-15.2972,0.0861887,9.36402))
        self.AddShadowTriangle((-15.2972,0.0861887,9.36402), (-15.2972,2.39342,9.36402), (-15.2972,2.39342,-2.38))
        self.AddShadowTriangle((2.38,0.0861887,15.2915), (2.38,2.39342,15.2915), (-9.36967,2.39342,15.2915))
        self.AddShadowTriangle((-9.36967,2.39342,15.2915), (-9.36967,0.0861887,15.2915), (2.38,0.0861887,15.2915))
        self.AddShadowTriangle((-9.36967,2.39342,15.2915), (-15.2972,2.39342,9.36402), (-15.2972,0.0861887,9.36402))
        self.AddShadowTriangle((-9.36967,2.39342,15.2915), (-15.2972,0.0861887,9.36402), (-9.36967,0.0861887,15.2915))
        
    def HazardsOn(self, on):
        if on:
            self.flame4a = Hazards.Flame((-3.71, -.83, -6.26), (0, 7, 0), (.2, .4, .2), 1)
            self.AddHazard(self.flame4a)
            self.flame4b = Hazards.Flame((-5.96, -.83, -3.49), (0, 7, 0), (.2, .4, .2), 1)
            self.AddHazard(self.flame4b)
            self.flame5a = Hazards.Flame((3.66, -.83, 6.18), (0, 7, 0), (.2, .4, .2), 1)
            self.AddHazard(self.flame5a)
            self.flame5b = Hazards.Flame((5.92, -.83, 3.47), (0, 7, 0), (.2, .4, .2), 1)
            self.AddHazard(self.flame5b)
            
            prism = self.AddPrismatic("Collision Box", "SpikeA Collision", 0, 1, 0, 0, 1.5, 0)
            self.spikes1 = Hazards.Spikes(prism, 50000, (-4.56, 0, 4.71))
            prism = self.AddPrismatic("Collision Box", "SpikeB Collision", 0, 1, 0, 0, 1.5, 0)
            self.spikes2 = Hazards.Spikes(prism, 50000, (4.67, 0, -4.59))
            
            self.RegisterZone("Spike_ZoneA",2)
            self.RegisterZone("Spike_ZoneB",3)
            self.RegisterZone("Flame_ZoneA",4)
            self.RegisterZone("Flame_ZoneB",5)
            self.SetSubMaterialSound("SpikeA Collision", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("SpikeB Collision", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            
            self.AddCollisionLine((-9.4, 2.4), (-2.4, 9.4))
            self.AddCollisionLine((2.4, 9.4), (9.4, 2.4))
            self.AddCollisionLine((9.4, -2.4), (2.4, -9.5))
            self.AddCollisionLine((-9.4, -2.4), (-2.4, -9.5))
        
        self.AddCollisionLine((-2.4, 9.4), (-2.4, 2.4))
        self.AddCollisionLine((-2.4, 2.4), (-9.4, 2.4))
        
        self.AddCollisionLine((2.4, 9.4), (2.4, 2.4))
        self.AddCollisionLine((2.4, 2.4), (9.4, 2.4))
        
        self.AddCollisionLine((2.4, -2.4), (9.4, -2.4))
        self.AddCollisionLine((2.4, -2.4), (2.4, -9.5))
        
        self.AddCollisionLine((-9.4, -2.4), (-2.4, -2.4))
        self.AddCollisionLine((-2.4, -2.4), (-2.4, -9.5))
        
        # walls
        self.AddCollisionLine((2.4, 15.3), (-9.3, 15.2))
        self.AddCollisionLine((-9.3, 15.2), (-15.2, 9.3))
        self.AddCollisionLine((-15.2, 9.3), (-15.2, -2.3))
        self.AddCollisionLine((-15.2, -2.3), (-2.3, -15.2))
        self.AddCollisionLine((-2.3, -15.2), (9.3, -15.2))
        self.AddCollisionLine((9.3, -15.2), (15.2, -9.5))
        self.AddCollisionLine((15.2, -9.5), (15.2, 2.3))
        self.AddCollisionLine((15.2, 2.3), (2.4, 15.3))
        
        self.AddPOV(0, (0, 13), (1, 4, 7))
        self.AddPOV(1, (7.5, 7.5), (0, 2))
        self.AddPOV(2, (13, 0), (1, 3, 6))
        self.AddPOV(3, (7.5, -8), (2, 4))
        self.AddPOV(4, (0, -13), (0, 3, 5))
        self.AddPOV(5, (-7.5, -7.5), (4, 6))
        self.AddPOV(6, (-13, 0), (2, 5, 7))
        self.AddPOV(7, (-8, 8), (0, 6))
        
        return Arenas.SuperArena.HazardsOn(self, on)

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-24.7415,25.1133,-29.1943)
        plus.setCameraRotation(0.615261,0.704592)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/smell_glue.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Hilltop_Welcome.wav", "Sounds/announcers/Arena_Hilltop_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Hilltop_AreYouWorthyToBeKing.wav", "Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Clawtop_PushingIntoFlames.wav", "Sounds/announcers/Hazard_Fire_GooseCooked.wav", "Sounds/announcers/Hazard_Fire_WatchFlames.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-24.7415,25.1133,-29.1943), (0.615261,0.704592), 0.675, (-14.848,18.8305,15.3655), (0.767187,2.37905), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((15.0829,14.9498,-2.50329), (1.00864,-1.76483), 0.675, (8.27242,9.03776,-8.10172), (1.13697,-0.786874), 0.675, 0, 2)
            plus.animateCamera((-10.6987,5.09156,-10.3803), (0.524423,0.803653), 0.675, (-8.69213,12.7842,-8.36998), (1.13439,0.812802), 0.675, 2, 4)
            plus.animateCamera((11.7741,15.1004,0.0835621), (0.841642,-1.57107), 0.675, (6.27404,11.2405,0.0835622), (0.978884,-1.57131), 0.675, 4, 6)
            yield 6

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((0.0348502,8.63033,3.0538), (0.735124,0.0), 0.675, (0.0348502,5.02771,7.03817), (0.735124,0.0), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((0.0348476,8.79597,-2.72149), (0.73107,3.13506), 0.675, (0.0585011,5.55021,-6.34049), (0.73107,3.13506), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((2.79119,8.79722,0.0348791), (0.744325,1.57751), 0.675, (6.64487,5.2477,0.0090155), (0.744325,1.57751), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-2.40099,8.86506,-0.09331), (0.719003,-1.5708), 0.675, (-5.9251,5.78039,-0.09331), (0.719003,-1.5708), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
 
    def Tick(self):
        # do our stuff here
        if self.bHazardsOn:
            self.spikes1.Tick()
            self.spikes2.Tick()
            self.flame4a.Tick()
            self.flame4b.Tick()
            self.flame5a.Tick()
            self.flame5b.Tick()
        
        return KingOfHill.Tick(self)
        
    def ZoneEvent(self, direction, id, robot, chassis):
        if id == 2:
            self.spikes1.ZoneEvent(direction)
        elif id == 3:
            self.spikes2.ZoneEvent(direction)
        elif id ==4:
            self.flame4a.ZoneEvent(direction)
            self.flame4b.ZoneEvent(direction)
        elif id == 5:
            self.flame5a.ZoneEvent(direction)
            self.flame5b.ZoneEvent(direction)
            
        return True
        
    def GetPath(self, start, end, ignore_hazards):
        # overridden to deal with getting out of hazard

        if ignore_hazards:
            return Arenas.SuperArena.GetPath(self, start, end, ignore_hazards)

        inHaz = InHazard(start)
        if inHaz == 0:
            return Arenas.SuperArena.GetPath(self, start, end, ignore_hazards)
            
        # pathfind out of hazards
        if inHaz == 1: # bot is in hazard 1
            path = Arenas.SuperArena.GetPath(self, (0, 0, 13), end, ignore_hazards)
            return ((0, 13),) + path
        elif inHaz == 2: # bot is in hazard 2
            path = Arenas.SuperArena.GetPath(self, (7.5, 0, -8), end, ignore_hazards)
            return ((7.5, -8),) + path
        elif inHaz == 3: # bot is in hazard 3
            path = Arenas.SuperArena.GetPath(self, (-7.5, 0, -7.5), end, ignore_hazards)
            return ((-7.5, -7.5),) + path
        elif inHaz == 4: #bot is in hazard 4
            path  = Arenas.SuperArena.GetPath(self, (-8, 0, 8), end, ignore_hazards)
            return ((-8, 8),) + path
            
        return Arenas.SuperArena.GetPath(self, start, end, ignore_hazards)
            
Arenas.register(HilltopArena)
