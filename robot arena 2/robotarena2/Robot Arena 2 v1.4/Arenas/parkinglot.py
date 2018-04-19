from __future__ import generators
import plus
import Arenas
import Hazards
import random

class LotArena(Arenas.SuperArena):
    "This unofficial downtown arena draws great competition from locals and visitors. Home-made hazards include platforms of cinder blocks that are dumped on the robots."
    name = "Parking Lot"
    preview = "parkinglot/parkinglot_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-12, 11, 11, -27)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/parkinglot/parkinglot.gmf")
        plus.setBackColor(.36, .537, .788)
        
        fov = 0.015
        self.AddStaticCamera("Static Cam 1", (-21.5, 13.0, -15.92), (0.47, 1.33), 78*fov)
        self.AddStaticCamera("Static Cam 2", (1.5, 10.6, 24.48), (0.253, 3.13), 57*fov)
        self.AddStaticCamera("Static Cam 3", (21.32, 13.0, 7.53), (0.38, -2.05), 77*fov)
        self.AddWatchCamera("Watch Cam 1", (-10.7, 7.2, -15.04), (1,8, 80*fov, 63*fov))
        self.AddWatchCamera("Watch Cam 2", (5.79, 7.27, -18.73), (14,18, 68*fov, 40*fov))

    def AddShadowReceivers(self):
        self.SetShadowSource(-1.953, 64.856, 46.457)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((-9.87727,0.102301,11.4006), (9.80893,0.102301,-26.5166), (9.95034,0.102301,11.3963))
        self.AddShadowTriangle((-9.87995,0.102301,-11.9232), (9.80893,0.102301,-26.5166), (-9.87727,0.102301,11.4006))
        self.AddShadowTriangle((-9.87995,0.102301,-11.9232), (-12.2699,0.102301,-26.5166), (9.80893,0.102301,-26.5166))
        self.AddShadowTriangle((-9.87995,0.102301,-11.9232), (-12.5444,0.102301,-14.6409), (-12.2699,0.102301,-26.5166))
        
    def HazardsOn(self, on):
        if on:
            hinge = self.GetHinge("Hinge01")
            self.trapdoor1 = Hazards.TrapDoor(hinge, (-0.73, 0, -24.74))
            self.AddHazard(self.trapdoor1)
            hinge = self.GetHinge("Hinge02")
            self.trapdoor2 = Hazards.TrapDoor(hinge, (-7.67, 0, -24.74))
            self.AddHazard(self.trapdoor2)
            self.RegisterZone("hazardzone1", 1)
            self.RegisterZone("hazardzone2", 2)
            i = 1
            while i<26:
                self.SetSubMaterialSound("cinderblock"+str(i), "metal", 1.0, "Sounds\\cinderblock1.wav")
                self.SetActive("cinderblock"+str(i), False)
                #self.SetPinned("cinderblock"+str(i), True)
                i += 1
                
            self.AddCollisionLine((-9.3, -23.8), (-6, -23.8))
            self.AddCollisionLine((-6, -23.8), (-6, -25.7))
            self.AddCollisionLine((-9.3, -23.8), (-9.3, -25.7))
            
            self.AddCollisionLine((-2.4, -23.8), (.9, -23.8))
            self.AddCollisionLine((.9, -23.8), (.9, -25.7))
            self.AddCollisionLine((-2.4, -23.8), (-2.4, -25.7))
                
        else:
            pass
            
        self.AddPOV(0, (0, -15), (1, 2))
        self.AddPOV(1, (-8, -19), (0, 2))
        self.AddPOV(2, (5, -19), (0, 1))
            
        self.AddCollisionLine((-4.4, -22.9), (-4.4, -26.6))
        self.AddCollisionLine((2.6, -22.9), (2.6, -26.6))
        
        self.AddCollisionLine((10, -10.6), (8.7, -10.6))
        self.AddCollisionLine((8.7, -10.6), (8.7, -12))
        self.AddCollisionLine((8.7, -12), (10, -12))
        
        self.AddCollisionLine((8.7, -17.2), (10, -17.2))
        self.AddCollisionLine((8.7, -17.2), (8.7, -18.7))
        self.AddCollisionLine((8.7, -18.7), (10, -18.7))

        # walls
        self.AddCollisionLine((-9.8, 11.4), (-9.8, -11.9))
        self.AddCollisionLine((-9.8, -11.9), (-12.5, -14.6))
        self.AddCollisionLine((-12.5, -14.6), (-12.2, -26.5))
        self.AddCollisionLine((-12.2, -26.5), (9.8, -26.5))
        self.AddCollisionLine((9.8, -26.5), (10, 11.4))
        self.AddCollisionLine((10, 11.4), (-9.8, 11.4))
        
        return Arenas.SuperArena.HazardsOn(self, on)

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(29.6173,13.1409,-34.943)
        plus.setCameraRotation(0.291095,-0.741162)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/tool_rage.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_ParkingLot_Welcome.wav", "Sounds/announcers/Arena_ParkingLot_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_ParkingLot_WatchOutForFallingObjects.wav", "Arena_NowhereToHide.wav", "Intro_ParkingLot_WhatABeautifulDay.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_ParkingLot_HitByTonOfBricks.wav",)
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((29.6173,13.1409,-34.943), (0.291095,-0.741162), 0.675, (20.2562,13.1409,18.2601), (0.354368,-2.53487), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-4.5069,0,-10.224), (-0.269276,-3.14159), 0.675, (-4.5069,17.4321,-17.1506), (1.07049,-3.14159), 0.675, 0, 6)
            yield 6

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((0.750588,4.35586,-1.97589), (0.580406,-2.46194), 0.675, (0.181229,2.56189,-5.45814), (0.571969,-2.00781), 0.675, 0, delaytime)
            yield delaytime
            
        if 1 in players:
            #bot 2 cam
            plus.animateCamera((-0.0178422,4.22551,-2.88332), (0.593309,0.818719), 0.675, (2.95787,2.47741,-2.74392), (0.50898,0.368722), 0.675, 0, delaytime)
            yield delaytime
            
        if 2 in players:
            #bot 3 cam
            plus.animateCamera((1.73748,3.83555,-3.11437), (0.49849,-0.83305), 0.675, (-1.88429,2.4499,-2.03161), (0.550847,-0.410693), 0.675, 0, delaytime)
            yield delaytime
            
        if 3 in players:
            #bot 4 cam
            plus.animateCamera((0.442939,4.22231,-1.84856), (0.563456,2.46685), 0.675, (0.889469,2.61047,-5.71382), (0.582065,1.91902), 0.675, 0, delaytime)
            yield delaytime
            
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0

    def Tick(self):
        "Do our stuff here -- called every tickInterval seconds."
            
        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        #print "robot:", robot
        if id == 1:
            if self.trapdoor1.Trigger():
                for i in range(1,15): self.SetActive("cinderblock"+str(i), True)
        elif id == 2:
            if self.trapdoor2.Trigger():
                for i in range(15,26): self.SetActive("cinderblock"+str(i), True)
            
        return True


Arenas.register(LotArena)
