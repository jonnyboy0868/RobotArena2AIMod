from __future__ import generators
import plus
import Arenas
import random
import Hazards
import math

class ClawTop(Arenas.SuperArena):
    "Made especially for tabletop matches, the ClawTop Arena features several flame hazards and a pair of rotating claws that will force your bot over the edge if you get too close."
    name = "ClawTop"
    preview = "tabletop/clawtop_preview.bmp"
    game_types = ['TABLETOP']
    extent = (-13, 13, 14, -14)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/tabletop/clawtop.gmf")
        #plus.Arena.__init__(self, "")
        plus.setBackColor(0,0,0)
        
        fov = 0.015
        self.AddStaticCamera("Static Cam 1", (5.15, 9.1, -24.75), ( 0.3196,-0.208), 63*fov)
        self.AddStaticCamera("Static Cam 2", (0.75, 24.8, -0.06), (1.5708,0), 72*fov)
        self.AddWatchCamera("Watch Cam 1", (2.257, 6, -19.04), (10, 18, 55*fov, 20*fov))
        self.AddWatchCamera("Watch Cam 2", (0, 8.5, 0), (8, 15, 80*fov, 60*fov))
        self.players = ()
        
    def __del__(self):
        if self.bHazardsOn:
            plus.removeSound(self.ambience)
        Arenas.SuperArena.__del__(self)
        
    def AddShadowReceivers(self):
        self.SetShadowSource(5.897, 19.159, 5.899)
        
        #Main Arena Floor Shadow Triangles
        self.AddShadowTriangle((-10.2877,0.676244,1.83754), (-12.4182,0.676244,12.4283), (-12.4182,0.676244,1.83754))
        self.AddShadowTriangle((-8.17686,0.676244,9.91855), (-8.17686,0.676244,12.4283), (-12.4182,0.676244,12.4283))
        self.AddShadowTriangle((-8.17686,0.676244,9.91855), (-12.4182,0.676244,12.4283), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((2.25999,0.676244,12.4283), (-2.49123,0.676244,12.4283), (-2.49123,0.676244,9.91855))
        self.AddShadowTriangle((2.25999,0.676244,9.91855), (2.25999,0.676244,12.4283), (-2.49123,0.676244,9.91855))
        self.AddShadowTriangle((12.413,0.676244,12.4283), (7.93297,0.676244,12.4283), (7.93297,0.676244,9.91855))
        self.AddShadowTriangle((10.2878,0.676244,1.91641), (12.413,0.676244,12.4283), (7.93297,0.676244,9.91855))
        self.AddShadowTriangle((10.2878,0.676244,1.91641), (12.413,0.676244,1.91641), (12.413,0.676244,12.4283))
        self.AddShadowTriangle((8.17711,0.676244,-9.92447), (12.413,0.676244,-12.4279), (10.2878,0.676244,-1.93329))
        self.AddShadowTriangle((10.2878,0.676244,-1.93329), (12.413,0.676244,-12.4279), (12.413,0.676244,-1.93329))
        self.AddShadowTriangle((8.17711,0.676244,-9.92447), (8.17711,0.676244,-12.4279), (12.413,0.676244,-12.4279))
        self.AddShadowTriangle((-2.26871,0.676244,-12.4279), (2.49519,0.676244,-12.4279), (2.49519,0.676244,-9.92447))
        self.AddShadowTriangle((-2.26871,0.676244,-9.92447), (-2.26871,0.676244,-12.4279), (2.49519,0.676244,-9.92447))
        self.AddShadowTriangle((-12.4182,0.676244,-12.4279), (-7.93688,0.676244,-12.4279), (-7.93688,0.676244,-9.92447))
        self.AddShadowTriangle((-10.2877,0.676244,-1.8361), (-12.4182,0.676244,-12.4279), (-7.93688,0.676244,-9.92447))
        self.AddShadowTriangle((-10.2877,0.676244,-1.8361), (-12.4182,0.676244,-1.8361), (-12.4182,0.676244,-12.4279))
        self.AddShadowTriangle((-2.49123,0.676244,9.91855), (-8.17686,0.676244,9.91855), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((2.49519,0.676244,-9.92447), (8.17711,0.676244,-9.92447), (10.2878,0.676244,-1.93329))
        self.AddShadowTriangle((10.2878,0.676244,-1.93329), (-10.2877,0.676244,-1.8361), (-2.26871,0.676244,-9.92447))
        self.AddShadowTriangle((10.2878,0.676244,1.91641), (7.93297,0.676244,9.91855), (2.25999,0.676244,9.91855))
        self.AddShadowTriangle((2.25999,0.676244,9.91855), (-2.49123,0.676244,9.91855), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((10.2878,0.676244,1.91641), (2.25999,0.676244,9.91855), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((10.2878,0.676244,-1.93329), (10.2878,0.676244,1.91641), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((-10.2877,0.676244,-1.8361), (10.2878,0.676244,-1.93329), (-10.2877,0.676244,1.83754))
        self.AddShadowTriangle((-2.26871,0.676244,-9.92447), (2.49519,0.676244,-9.92447), (10.2878,0.676244,-1.93329))
        self.AddShadowTriangle((-10.2877,0.676244,-1.8361), (-7.93688,0.676244,-9.92447), (-2.26871,0.676244,-9.92447))
        
        #Hazard Shadow Triangles
        self.AddShadowTriangle((-8.0217,0.407085,-12.2193), (-2.21868,0.407085,-12.2193), (-2.21868,0.407085,-9.90302))
        self.AddShadowTriangle((-2.21868,0.407085,-9.90302), (-8.0217,0.407085,-9.90302), (-8.0217,0.407085,-12.2193))
        self.AddShadowTriangle((2.42165,0.407085,-12.2193), (8.22466,0.407085,-12.2193), (8.22466,0.407085,-9.90302))
        self.AddShadowTriangle((8.22466,0.407085,-9.90302), (2.42165,0.407085,-9.90302), (2.42165,0.407085,-12.2193))
        self.AddShadowTriangle((-8.24321,0.407085,9.84521), (-2.4402,0.407085,9.84521), (-2.4402,0.407085,12.1615))
        self.AddShadowTriangle((-2.4402,0.407085,12.1615), (-8.24321,0.407085,12.1615), (-8.24321,0.407085,9.84521))
        self.AddShadowTriangle((2.20013,0.407085,9.84521), (8.00315,0.407085,9.84521), (8.00315,0.407085,12.1615))
        self.AddShadowTriangle((8.00315,0.407085,12.1615), (2.20013,0.407085,12.1615), (2.20013,0.407085,9.84521))
        
    def Activate(self, on):
        if on: self.players = plus.getPlayers()
        
        Arenas.SuperArena.Activate(self, on)
        
    def HazardsOn(self, on):
        if on:
            self.flame4a = Hazards.Flame((-3.96, -.19, -11.04), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame4a)
            self.flame4b = Hazards.Flame((-6.23, -.19, -11.04), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame4b)
            self.flame3a = Hazards.Flame((4.21, -.19, -11.04), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame3a)
            self.flame3b = Hazards.Flame((6.47, -.19, -11.04), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame3b)
            self.flame1a = Hazards.Flame((-6.37, -.19, 11), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame1a)
            self.flame1b = Hazards.Flame((-4.1, -.19, 11), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame1b)
            self.flame2a = Hazards.Flame((4.06, -.19, 11), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame2a)
            self.flame2b = Hazards.Flame((6.33, -.19, 11), (0, 7, 0), (.2, .4, .2), .8)
            self.AddHazard(self.flame2b)
        
            self.ambience = plus.createSound("Sounds/hzd_rotclaw_loop.wav", False, (0, 0, 0))
            plus.loopSound(self.ambience)
            
            self.RegisterZone("flamezone01",1)
            self.RegisterZone("flamezone02",2)
            self.RegisterZone("flamezone03",3)
            self.RegisterZone("flamezone04",4)
            
            self.claw1 = self.GetHinge("Hinge01")
            self.claw1.SetAutoLocks(False, True)
            self.claw1.SetPowerSettings(2, 1000)
            self.claw1.Lock(False)
            self.claw1.SetDirection(-100)
            
            self.claw2 = self.GetHinge("Hinge02")
            self.claw2.SetAutoLocks(False, True)
            self.claw2.SetPowerSettings(2, 1000)
            self.claw2.Lock(False)
            self.claw2.SetDirection(-100)
            
            self.AddCollisionLine((-8.2, 12.4), (-8.2, 9.9))
            self.AddCollisionLine((-8.2, 9.9), (-2.5, 9.9))
            self.AddCollisionLine((-2.5, 9.9), (-2.5, 12.4))
            
            self.AddCollisionLine((2.3, 12.4), (2.3, 9.9))
            self.AddCollisionLine((2.3, 9.9), (8, 9.9))
            self.AddCollisionLine((8, 9.9), (8, 12.4))
            
            self.AddCollisionLine((-7.9, -12.4), (-7.9, -9.9))
            self.AddCollisionLine((-7.9, -9.9), (-2.3, -9.9))
            self.AddCollisionLine((-2.3, -9.9), (-2.3, -12.4))
            
            self.AddCollisionLine((2.5, -12.4), (2.5, -9.9))
            self.AddCollisionLine((2.5, -9.9), (8.2, -9.9))
            self.AddCollisionLine((8.2, -9.9), (8.2, -12.4))
            
            self.AddCollisionLine((-12.4, 1.8), (-8.5, 1.8))
            self.AddCollisionLine((-8.5, 1.8), (-8.5, -1.8))
            self.AddCollisionLine((-8.5, -1.8), (-12.4, -1.8))
            
            self.AddCollisionLine((8.5, 1.8), (12.4, 1.8))
            self.AddCollisionLine((8.5, 1.8), (8.5, -1.8))
            self.AddCollisionLine((8.5, -1.8), (12.4, -1.8))            
        else:
            self.AddCollisionLine((-12.4, 1.8), (-10.3, 1.8))
            self.AddCollisionLine((-10.3, 1.8), (-10.3, -1.8))
            self.AddCollisionLine((-10.3, -1.8), (-12.4, -1.8))
            
            self.AddCollisionLine((10.3, 1.8), (12.4, 1.8))
            self.AddCollisionLine((10.3, 1.8), (10.3, -1.8))
            self.AddCollisionLine((10.3, -1.8), (12.4, -1.8))

        # walls
        self.AddCollisionLine((-11.4, 12.4), (-12.4, 11.4))
        self.AddCollisionLine((-12.4, 11.4), (-12.4, -11.4))
        self.AddCollisionLine((-12.4, -11.4), (-11.4, -12.4))
        self.AddCollisionLine((-11.4, -12.4), (11.4, -12.4))
        self.AddCollisionLine((11.4, -12.4), (12.4, -11.4))
        self.AddCollisionLine((12.4, -11.4), (12.4, 11.4))
        self.AddCollisionLine((12.4, 11.4), (11.4, 12.4))
        self.AddCollisionLine((11.4, 12.4), (-11.4, 12.4))
        
        self.AddPOV(0, (0, 0), (1, 2, 3, 4))
        self.AddPOV(1, (10.5, -7), (0,))
        self.AddPOV(2, (-10, -7), (0,))
        self.AddPOV(3, (10.5, 6.5), (0,))
        self.AddPOV(4, (-10.5, 6.5), (0,))
        
        return Arenas.SuperArena.HazardsOn(self, on)
            
    def Introduction(self):
        sounds = self.intro_sounds
        
        # set initial camera & fade from black
        plus.setCameraPosition(-11.6853,5.11775,-24.8297)
        plus.setCameraRotation(0.190675,0.481754)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)
        
        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/aggression.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Clawtop_Welcome.wav", "Sounds/announcers/Arena_Clawtop_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Clawtop_FlamesWillLeaveMarks.wav", "Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_Clawtop_ReachOutAndGrab.wav", "Intro_HoldOnToYourSeats.wav", "Intro_Clawtop_SpeaksSoftlyBigClaws.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Clawtop_AvoidRazorSharpClaws.wav", "Sounds/announcers/Hazard_Clawtop_ClawsToYourAdvantage.wav", "Sounds/announcers/Hazard_Clawtop_PushingIntoFlames.wav", "Sounds/announcers/Hazard_Fire_GooseCooked.wav", "Sounds/announcers/Hazard_Fire_WatchFlames.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-11.6853,5.11775,-24.8297), (0.190675,0.481754), 0.675, (24.8318,14.4726,3.01025), (0.531457,-1.74816), 0.825, 0, 9)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 2
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((32.278,14.7693,-7.88775), (0.57965,-1.20653), 0.675, (13.6977,8.51049,-6.08429), (0.902695,-0.381328), 0.675, 0, 2.5)
            plus.animateCamera((-5.04925,10.955,-14.1298), (1.31098,0.0), 0.675, (-5.04925,2.04966,-20.5915), (0.22594,0.0), 0.675, 2.5, 5)
            yield 5

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-7.71974,10.5449,7.02807), (0.99459,2.28536), 0.675, (-7.71974,3.83275,7.02807), (0.510025,2.28536), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((7.10965,7.44489,-6.53137), (0.880594,-0.843714), 0.675, (7.10965,2.36013,-6.53137), (0.366589,-0.843714), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((-6.62075,8.71118,-6.76299), (0.963239,0.776806), 0.675, (-6.62075,2.72167,-6.76299), (0.422321,0.776806), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((7.87338,8.80651,7.69725), (0.857608,-2.34843), 0.675, (7.87338,2.45089,7.69725), (0.31125,-2.34843), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0

    def Tick(self):
        # check to see if anyone has been "eliminated" by falling off the tabletop
        for each in self.players:
            if plus.getLocation(each)[1] < -4:
                plus.eliminatePlayer(each)

        if self.bHazardsOn:
            self.flame1a.Tick()
            self.flame1b.Tick()
            self.flame2a.Tick()
            self.flame2b.Tick()
            self.flame3a.Tick()
            self.flame3b.Tick()
            self.flame4a.Tick()
            self.flame4b.Tick()
        
        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        if id ==1:
            self.flame1a.ZoneEvent(direction)
            self.flame1b.ZoneEvent(direction)
        elif id == 2:
            self.flame2a.ZoneEvent(direction)
            self.flame2b.ZoneEvent(direction)
        elif id == 3:
            self.flame3a.ZoneEvent(direction)
            self.flame3b.ZoneEvent(direction)
        elif id == 4:
            self.flame4a.ZoneEvent(direction)
            self.flame4b.ZoneEvent(direction)
        return True

    def DistanceToEdge(self, location):
        min_dist = 999
        min_heading = 0
        
        dist = location[0] - -10.5
        if dist < min_dist:
            min_dist = dist
            min_heading = -math.pi / 2
        dist = 10.5 - location[0]
        if dist < min_dist:
            min_dist = dist
            min_heading = math.pi / 2
        dist = location[2] - -10.5
        if dist < min_dist:
            min_dist = dist
            min_heading = math.pi
        dist = 10.5 - location[2]
        if dist < min_dist:
            min_dist = dist
            min_heading = 0
        
        return (min_dist, min_dist <= 0, min_heading)

    def HeadingAwayFromEdge(self, location):
        dist, over, h = self.DistanceToEdge(location)
        
        return h + math.pi
        
Arenas.register(ClawTop)
