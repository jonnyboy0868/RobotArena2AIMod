from __future__ import generators
import plus
import Arenas
import Hazards
import random

class OctArena(Arenas.SuperArena):
    "You'll find hammers and hellraisers in this recessed arena. The starting blocks also slide away, revealing deathpits."
    name = "The Octagon"
    preview = "octagon/oct_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-22, 22, 23, -23)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/octagon/octagon.gmf")
        plus.setBackColor(0,0,0)
        
        startblock = self.AddPrismatic("main_collision", "startblock1", 0.707, 0, -0.707, 0, -3.8, 0)
        self.Pit1 = Hazards.PitSlider(startblock, 45, (-8.77, 0, 8.31))
        self.AddHazard(self.Pit1)
        startblock = self.AddPrismatic("main_collision", "startblock2", -0.707, 0, 0.707, 0, -3.8, 0)
        self.Pit2 = Hazards.PitSlider(startblock, 45, (8.67, 0, -8.61))
        self.AddHazard(self.Pit2)
        startblock = self.AddPrismatic("main_collision", "startblock3", -0.707, 0, -0.707, 0, -3.8, 0)
        self.Pit3 = Hazards.PitSlider(startblock, 45, (8.67, 0, 8.62))
        self.AddHazard(self.Pit3)
        startblock = self.AddPrismatic("main_collision", "startblock4", 0.707, 0, 0.707, 0, -3.8, 0)
        self.Pit4 = Hazards.PitSlider(startblock, 45, (-8.77, 0, -8.31))
        self.AddHazard(self.Pit4)
        
        # Static and Watch Camera Setup
        fov = 0.015
        self.AddStaticCamera("Static Cam 1", (-11, 9.66, -20.68), (0.305, 0.48), 65*fov)
        self.AddStaticCamera("Static Cam 2", (0, 27.13, 0), (1.5708, 0), 70*fov)
        self.AddWatchCamera("Watch Cam 1", (-14.45, 5.1, -6.23), (6,20,70*fov, 45*fov))
        self.AddWatchCamera("Watch Cam 1", (0.6, 5.0, -1.24), (2,8,70*fov, 55*fov))
        
        self.players = ()
        
    def AddShadowReceivers(self):
        self.SetShadowSource(7.513, 15.457, 19.314)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((8.77512,-0.102412,5.56215), (13.7884,-0.102412,-5.71206), (13.7887,-0.102412,5.71114))
        self.AddShadowTriangle((5.24311,-0.102412,9.07585), (7.8447,-0.102412,11.6564), (5.71206,-0.102412,13.7884))
        self.AddShadowTriangle((5.24311,-0.102412,9.07585), (5.71206,-0.102412,13.7884), (-5.56215,-0.102412,8.77512))
        self.AddShadowTriangle((8.77512,-0.102412,5.56215), (5.24311,-0.102412,9.07585), (5.56215,-0.102412,-8.77512))
        self.AddShadowTriangle((8.77512,-0.102412,5.56215), (5.56215,-0.102412,-8.77512), (9.07585,-0.102412,-5.24311))
        self.AddShadowTriangle((11.3547,-0.102412,8.1503), (8.77512,-0.102412,5.56215), (13.7887,-0.102412,5.71114))
        self.AddShadowTriangle((-5.56215,-0.102412,8.77512), (5.71206,-0.102412,13.7884), (-5.71114,-0.102412,13.7887))
        self.AddShadowTriangle((-9.07585,-0.102412,5.24311), (-11.6564,-0.102412,7.8447), (-13.7884,-0.102412,5.71206))
        self.AddShadowTriangle((-8.77512,-0.102412,-5.56215), (-13.7884,-0.102412,5.71206), (-13.7887,-0.102412,-5.71114))
        self.AddShadowTriangle((5.24311,-0.102412,9.07585), (-9.07585,-0.102412,5.24311), (-8.77512,-0.102412,-5.56215))
        self.AddShadowTriangle((-5.56215,-0.102412,8.77512), (-9.07585,-0.102412,5.24311), (5.24311,-0.102412,9.07585))
        self.AddShadowTriangle((-8.1503,-0.102412,11.3547), (-5.56215,-0.102412,8.77512), (-5.71114,-0.102412,13.7887))
        self.AddShadowTriangle((-8.77512,-0.102412,-5.56215), (-9.07585,-0.102412,5.24311), (-13.7884,-0.102412,5.71206))
        self.AddShadowTriangle((-5.24311,-0.102412,-9.07585), (-7.8447,-0.102412,-11.6564), (-5.71206,-0.102412,-13.7884))
        self.AddShadowTriangle((-5.24311,-0.102412,-9.07585), (-5.71206,-0.102412,-13.7884), (5.56215,-0.102412,-8.77512))
        self.AddShadowTriangle((-8.77512,-0.102412,-5.56215), (-5.24311,-0.102412,-9.07585), (5.56215,-0.102412,-8.77512))
        self.AddShadowTriangle((-8.77512,-0.102412,-5.56215), (5.56215,-0.102412,-8.77512), (5.24311,-0.102412,9.07585))
        self.AddShadowTriangle((-11.3547,-0.102412,-8.1503), (-8.77512,-0.102412,-5.56215), (-13.7887,-0.102412,-5.71114))
        self.AddShadowTriangle((5.56215,-0.102412,-8.77512), (-5.71206,-0.102412,-13.7884), (5.71114,-0.102412,-13.7887))
        self.AddShadowTriangle((9.07585,-0.102412,-5.24311), (11.6564,-0.102412,-7.8447), (13.7884,-0.102412,-5.71206))
        self.AddShadowTriangle((9.07585,-0.102412,-5.24311), (13.7884,-0.102412,-5.71206), (8.77512,-0.102412,5.56215))
        self.AddShadowTriangle((8.1503,-0.102412,-11.3547), (5.56215,-0.102412,-8.77512), (5.71114,-0.102412,-13.7887))
        self.AddShadowTriangle((13.7884,1.82678,-5.71206), (13.7887,1.82678,5.71115), (13.7887,-0.102412,5.71114))
        self.AddShadowTriangle((13.7887,-0.102412,5.71114), (13.7884,-0.102412,-5.71206), (13.7884,1.82678,-5.71206))
        self.AddShadowTriangle((7.8447,1.82678,11.6564), (5.71206,1.82678,13.7884), (5.71206,-0.102412,13.7884))
        self.AddShadowTriangle((5.71206,-0.102412,13.7884), (7.8447,-0.102412,11.6564), (7.8447,1.82678,11.6564))
        self.AddShadowTriangle((13.7887,1.82678,5.71115), (11.3547,1.82678,8.1503), (11.3547,-0.102412,8.1503))
        self.AddShadowTriangle((11.3547,-0.102412,8.1503), (13.7887,-0.102412,5.71114), (13.7887,1.82678,5.71115))
        self.AddShadowTriangle((5.71206,1.82678,13.7884), (-5.71114,1.82678,13.7887), (-5.71114,-0.102412,13.7887))
        self.AddShadowTriangle((-5.71114,-0.102412,13.7887), (5.71206,-0.102412,13.7884), (5.71206,1.82678,13.7884))
        self.AddShadowTriangle((-11.6564,1.82678,7.8447), (-13.7884,1.82678,5.71206), (-13.7884,-0.102412,5.71206))
        self.AddShadowTriangle((-13.7884,-0.102412,5.71206), (-11.6564,-0.102412,7.8447), (-11.6564,1.82678,7.8447))
        self.AddShadowTriangle((-5.71114,1.82678,13.7887), (-8.1503,1.82678,11.3547), (-8.1503,-0.102412,11.3547))
        self.AddShadowTriangle((-8.1503,-0.102412,11.3547), (-5.71114,-0.102412,13.7887), (-5.71114,1.82678,13.7887))
        self.AddShadowTriangle((-13.7884,1.82678,5.71206), (-13.7887,1.82678,-5.71114), (-13.7887,-0.102412,-5.71114))
        self.AddShadowTriangle((-13.7887,-0.102412,-5.71114), (-13.7884,-0.102412,5.71206), (-13.7884,1.82678,5.71206))
        self.AddShadowTriangle((-7.8447,1.82678,-11.6564), (-5.71206,1.82678,-13.7884), (-5.71206,-0.102412,-13.7884))
        self.AddShadowTriangle((-5.71206,-0.102412,-13.7884), (-7.8447,-0.102412,-11.6564), (-7.8447,1.82678,-11.6564))
        self.AddShadowTriangle((-13.7887,1.82678,-5.71114), (-11.3547,1.82678,-8.1503), (-11.3547,-0.102412,-8.1503))
        self.AddShadowTriangle((-11.3547,-0.102412,-8.1503), (-13.7887,-0.102412,-5.71114), (-13.7887,1.82678,-5.71114))
        self.AddShadowTriangle((-5.71206,1.82678,-13.7884), (5.71114,1.82678,-13.7887), (5.71114,-0.102412,-13.7887))
        self.AddShadowTriangle((5.71114,-0.102412,-13.7887), (-5.71206,-0.102412,-13.7884), (-5.71206,1.82678,-13.7884))
        self.AddShadowTriangle((11.6564,1.82678,-7.8447), (13.7884,1.82678,-5.71206), (13.7884,-0.102412,-5.71206))
        self.AddShadowTriangle((13.7884,-0.102412,-5.71206), (11.6564,-0.102412,-7.8447), (11.6564,1.82678,-7.8447))
        self.AddShadowTriangle((5.71114,1.82678,-13.7887), (8.1503,1.82678,-11.3547), (8.1503,-0.102412,-11.3547))
        self.AddShadowTriangle((8.1503,-0.102412,-11.3547), (5.71114,-0.102412,-13.7887), (5.71114,1.82678,-13.7887))
        
    def Activate(self, on):
        if on: self.players = plus.getPlayers()
        if on:
            if self.bHazardsOn:
                self.Pit1.setactive(True)
                self.Pit2.setactive(True)
                self.Pit3.setactive(True)
                self.Pit4.setactive(True)
        return Arenas.SuperArena.Activate(self, on)
                
    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-18.3694,10.7193,-18.9036)
        plus.setCameraRotation(0.273704,0.813325)
        plus.setCameraFOV(45)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/whatgame_loop.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .5
        
        #welcome to arena (load all sounds now to decrease lag later)
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))

        arenaOpt = ("Sounds/announcers/Arena_Octagon_Welcome.wav", "Sounds/announcers/Arena_Octagon_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        sounds['hazards'] = plus.createSound("Sounds/announcers/Hazard_OctagonEverything.wav", False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-18.3694,10.7193,-18.9036), (0.273704,0.813325), 45, (15.3706,10.7193,-21.4037), (0.27792,-0.647428), 45, 0, 7)
        yield 3
        
        #secondary intro comment
        plus.fadeOutLoop(sounds['crowd'], 8000)
        plus.playSound(sounds['generic'])
        yield 4
        
        #hazard cams
        if self.bHazardsOn:
            plus.animateCamera((-12.2938,5.45186,1.71877), (0.182787,0.746338), 0.675, (11.9546,2.71985,6.22833), (0.0399611,-0.944844), 0.465, 0, 3)
            plus.animateCamera((16.4935,7.66633,-0.596993), (0.350502,-1.55504), 0.315, (17.4828,5.91874,-0.596993), (0.40248,-1.54704), 0.885, 3, 6)
            yield .5
            plus.playSound(sounds['hazards'])
            yield 5.5
        
        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-4.26501,2.26282,-3.00544), (0.173469,-0.190282), 0.8793, (2.22932,2.26282,3.39724), (0.181724,-1.28878), 0.6093, 0, delaytime)
            yield delaytime
            
        if 1 in players:
            #bot 2 cam
            plus.animateCamera((-4.00138,2.00669,-5.34849), (0.163484,1.60859), 0.675, (-0.849382,3.50541,-2.65736), (0.398552,1.9945), 0.675, 0, delaytime)
            yield delaytime
            
        if 2 in players:
            #bot 3 cam
            plus.animateCamera((1.23589,1.95065,-1.50871), (0.119728,0.522505), 0.8868, (-0.299681,1.95065,-0.727713), (0.116014,0.726596), 0.5868, 0, delaytime)
            yield delaytime
            
        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-2.00614,3.97656,-2.32284), (0.579104,-2.37049), 1.0218, (-0.897416,1.17021,-4.30382), (0.119285,-1.92632), 0.7818, 0, delaytime)
            yield delaytime
            
        #fade out music
        plus.fadeOutLoop(self.intro_music, 3000)
        yield 3
        
        # done
        yield 0
        
    def HazardsOn(self, on):
        if on:
            self.SetSubMaterialSound("hammer1", "metal", .8, "Sounds\\hzd_hammer_thud.wav")
            self.SetSubMaterialSound("hammer2", "metal", .8, "Sounds\\hzd_hammer_thud.wav")
        
            hinge = self.GetHinge("Hinge01")
            self.RegisterZone("hellzone1", 1)
            self.Hell1 = Hazards.HellRaiser(hinge, (-4.72, -0.15, -0.26))
            self.AddHazard(self.Hell1)
            
            hinge = self.GetHinge("Hinge02")
            self.RegisterZone("hellzone2", 2)
            self.Hell2 = Hazards.HellRaiser(hinge, (3.56, -0.15, -0.26))
            self.AddHazard(self.Hell2)
            
            hinge = self.GetHinge("hammerhinge1")
            self.RegisterZone("hammerzone1", 3)
            self.Hammer1 = Hazards.Hammer(hinge, (0, -0.26, -11.76))
            self.AddHazard(self.Hammer1)
            
            hinge = self.GetHinge("hammerhinge2")
            self.RegisterZone("hammerzone2", 4)
            self.Hammer2 = Hazards.Hammer(hinge, (0, -0.26, -8.31))
            self.AddHazard(self.Hammer2)
            
            # hammers
            self.AddCollisionLine((-1.1, -12.9), (-1.1, -10.6))
            self.AddCollisionLine((-1.1, -10.6), (1.1, -10.6))
            self.AddCollisionLine((1.1, -10.6), (1.1, -12.9))
            
            self.AddCollisionLine((1.1, 12.9), (1.1, 10.6))
            self.AddCollisionLine((1.1, 10.6), (-1.1, 10.6))
            self.AddCollisionLine((-1.1, 10.6), (-1.1, 12.9))
            
            # hellraisers
            self.AddCollisionLine((4, -1.4), (3.1, -1.4))
            self.AddCollisionLine((3.1, -1.4), (3.1, .9))
            self.AddCollisionLine((3.1, .9), (4, .9))
            self.AddCollisionLine((4, .9), (4, -1.4))
            
            self.AddCollisionLine((-4.3, -1.4), (-5.2, -1.4))
            self.AddCollisionLine((-5.2, -1.4), (-5.2, .9))
            self.AddCollisionLine((-5.2, .9), (-4.3, .9))
            self.AddCollisionLine((-4.3, .9), (-4.3, -1.4))
            
            # start pits
            self.AddCollisionLine((-11.4, -8.2), (-8.8, -5.6))
            self.AddCollisionLine((-8.8, -5.6), (-5.2, -9.1))
            self.AddCollisionLine((-5.2, -9.1), (-7.9, -11.7))
            
            self.AddCollisionLine((-11.7, 7.9), (-9.1, 5.2))
            self.AddCollisionLine((-9.1, 5.2), (-5.6, 8.8))
            self.AddCollisionLine((-5.6, 8.8), (-8.2, 11.4))
            
            self.AddCollisionLine((7.9, 11.7), (5.2, 9.1))
            self.AddCollisionLine((5.2, 9.1), (8.8, 5.6))
            self.AddCollisionLine((8.8, 5.6), (11.4, 8.2))
            
            self.AddCollisionLine((8.2, -11.4), (5.6, -8.8))
            self.AddCollisionLine((5.6, -8.8), (9.1, -5.2))
            self.AddCollisionLine((9.1, -5.2), (11.7, -7.9))
            
            self.AddPOV(0, (0, -6.5), (1, 4, 7))
            self.AddPOV(1, (-6.5, -4), (0, 2))
            self.AddPOV(2, (-10, 0), (1, 3))
            self.AddPOV(3, (-6.5, 4), (2, 4))
            self.AddPOV(4, (0, 6.5), (0, 3, 5))
            self.AddPOV(5, (6.5, 4), (4, 6))
            self.AddPOV(6, (10, 0), (5, 7))
            self.AddPOV(7, (6.5, -4), (0, 6))
        
        # walls
        self.AddCollisionLine((-5.7, 13.8), (-13.8, 5.7))
        self.AddCollisionLine((-13.8, 5.7), (-13.8, -5.7))
        self.AddCollisionLine((-13.8, -5.7), (-5.7, -13.8))
        self.AddCollisionLine((-5.7, -13.8), (5.7, -13.8))
        self.AddCollisionLine((5.7, -13.8), (13.8, -5.7))
        self.AddCollisionLine((13.8, -5.7), (13.8, 5.7))
        self.AddCollisionLine((13.8, 5.7), (5.7, 13.8))
        self.AddCollisionLine((5.7, 13.8), (-5.7, 13.8))
        
        return Arenas.SuperArena.HazardsOn(self, on)
        
    def Tick(self):
        # check to see if anyone has been "eliminated" by falling into a pit
        for each in self.players:
            if plus.getLocation(each)[1] < -1.5 and not plus.isEliminated(each):
                plus.eliminatePlayer(each)
                
        if self.bHazardsOn:
            self.Hell1.Tick()
            self.Hell2.Tick()
            self.Hammer1.Tick()
            self.Hammer2.Tick()
            self.Pit1.Tick()
            self.Pit2.Tick()
            self.Pit3.Tick()
            self.Pit4.Tick()
        
        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        if (id==1 and direction==1):
            self.Hell1.RaiseHell()
        if (id==2 and direction==1):
            self.Hell2.RaiseHell()
        if (id==3):
            self.Hammer1.ZoneEvent(direction)
        if (id==4):
            self.Hammer2.ZoneEvent(direction)
        return True

Arenas.register(OctArena)
