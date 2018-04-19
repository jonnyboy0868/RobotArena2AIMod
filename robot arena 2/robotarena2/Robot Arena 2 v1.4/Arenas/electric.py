from __future__ import generators
import plus
import Arenas
import random
import Hazards

class ElectricArena(Arenas.SuperArena):
    "You may want to watch out for the metal grid in the center of the arena.  Getting caught there at the wrong time could be a shocking experience."
    name = "Electric Arena"
    preview = "electric/dm_electric_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-16, 20, 17, -21)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/electric/electric.gmf")
        plus.setBackColor(0,0,0)
        
        # Static Cameras
        self.AddStaticCamera("Overhead", (0, 58, 0), (1.5708, 3.1514), 0.675)
        self.AddStaticCamera("Side", (-27, 42, 0), (0.9897, 1.575), 0.675)
        
        # Watch Cameras
        self.AddWatchCamera("Watch 1", (-14, 15, 18), (5.0, 30.0, 0.675, 0.375))
        
        self.chargetimer = 0.0
        self.zaptimer = 0.0
        
    def __del__(self):
        if self.bHazardsOn:
            plus.removeSound(self.ambience)
        Arenas.SuperArena.__del__(self)
        
    def AddShadowReceivers(self):
        self.SetShadowSource(1.448, 13.251, -11.357)
        
        #Main Arena Shadow Triangles
        self.AddShadowTriangle((-15.9886,-0.70284,-15.8668), (-11.9024,-0.70284,-19.9973), (16.0101,-0.70284,-15.8163))
        self.AddShadowTriangle((11.8704,-0.70284,-19.9973), (16.0101,-0.70284,-15.8163), (-11.9024,-0.70284,-19.9973))
        self.AddShadowTriangle((-15.9886,-0.70284,15.8838), (-15.9886,-0.70284,-15.8668), (16.0101,-0.70284,15.8298))
        self.AddShadowTriangle((16.0101,-0.70284,-15.8163), (16.0101,-0.70284,15.8298), (-15.9886,-0.70284,-15.8668))
        self.AddShadowTriangle((-11.9024,-0.70284,19.97), (-15.9886,-0.70284,15.8838), (11.9155,-0.70284,19.97))
        self.AddShadowTriangle((16.0101,-0.70284,15.8298), (11.9155,-0.70284,19.97), (-15.9886,-0.70284,15.8838))
        self.AddShadowTriangle((-11.9024,-0.70284,-19.9973), (-15.9886,-0.70284,-15.8668), (-11.9024,2.70996,-19.9973))
        self.AddShadowTriangle((-15.9886,2.70996,-15.8668), (-11.9024,2.70996,-19.9973), (-15.9886,-0.70284,-15.8668))
        self.AddShadowTriangle((11.8704,-0.70284,-19.9973), (-11.9024,-0.70284,-19.9973), (11.8704,2.70996,-19.9973))
        self.AddShadowTriangle((-11.9024,2.70996,-19.9973), (11.8704,2.70996,-19.9973), (-11.9024,-0.70284,-19.9973))
        self.AddShadowTriangle((16.0101,-0.70284,-15.8163), (11.8704,-0.70284,-19.9973), (16.0101,2.70996,-15.8163))
        self.AddShadowTriangle((11.8704,2.70996,-19.9973), (16.0101,2.70996,-15.8163), (11.8704,-0.70284,-19.9973))
        self.AddShadowTriangle((16.0101,-0.70284,15.8298), (16.0101,-0.70284,-15.8163), (16.0101,2.70996,15.8297))
        self.AddShadowTriangle((16.0101,2.70996,-15.8163), (16.0101,2.70996,15.8297), (16.0101,-0.70284,-15.8163))
        self.AddShadowTriangle((11.9155,-0.70284,19.97), (16.0101,-0.70284,15.8298), (11.9155,2.70996,19.97))
        self.AddShadowTriangle((16.0101,2.70996,15.8297), (11.9155,2.70996,19.97), (16.0101,-0.70284,15.8298))
        self.AddShadowTriangle((-11.9024,-0.70284,19.97), (11.9155,-0.70284,19.97), (-11.9024,2.70996,19.97))
        self.AddShadowTriangle((11.9155,2.70996,19.97), (-11.9024,2.70996,19.97), (11.9155,-0.70284,19.97))
        self.AddShadowTriangle((-15.9886,-0.70284,15.8838), (-11.9024,-0.70284,19.97), (-15.9886,2.70996,15.8838))
        self.AddShadowTriangle((-11.9024,2.70996,19.97), (-15.9886,2.70996,15.8838), (-11.9024,-0.70284,19.97))
        self.AddShadowTriangle((-15.9886,-0.70284,-15.8668), (-15.9886,-0.70284,15.8838), (-15.9886,2.70996,-15.8668))
        self.AddShadowTriangle((-15.9886,2.70996,15.8838), (-15.9886,2.70996,-15.8668), (-15.9886,-0.70284,15.8838))
        
    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-15.6905,16.0921,-0.205826)
        plus.setCameraRotation(0.42351,0.7542)
        plus.setCameraFOV(0.9)
        plus.fadeFromBlack(.25)
        
        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/embattled.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Electric_Welcome.wav", "Sounds/announcers/Arena_Electric_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Electric_HighVoltageAction.wav", "Intro_Electric_PrepareToBeZapped.wav", "Intro_Electric_WattsOfEnergy.wav", "Intro_Electric_BenFranklinDiscoverdElectricty.wav", "Intro_Electric_ShockingExperience.wav", "Intro_HoldOnToYourSeats.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Electric_ButtonSwitch.wav",)
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-15.6905,16.0921,-0.205826), (0.42351,0.7542), 0.9, (-15.6905,16.0921,-0.205826), (0.490898,2.50581), 0.9, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            print "hazard vo"
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-4.19939,4.9921,17.9282), (0.271605,1.58573), 0.675, (11.4895,4.9921,9.22499), (0.519623,0.258988), 0.675, 0, 2.5)
            plus.animateCamera((-14.6452,17.3103,-18.4424), (0.649154,0.678271), 0.675, (-10.2019,5.96188,-11.9301), (0.379119,0.720136), 0.675, 3, 6.5)
            yield 6.5

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((6.15679,0.804018,14.9727), (0.118508,-1.11342), 0.675, (0.278868,5.08238,10.9266), (0.625943,-0.0257021), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((0.00413038,5.3345,-10.8038), (0.622604,-3.14159), 0.675, (6.01218,1.37234,-16.0091), (0.211,-1.92562), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((-8.85391,3.17855,-0.0592491), (0.565296,-1.56135), 0.675, (-5.53554,3.17855,-4.36084), (0.326206,-1.08959), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((8.19485,2.12433,3.1667), (0.288549,2.02696), 0.675, (7.52027,5.29964,-1.96182), (0.623464,1.29934), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0 
        
    def HazardsOn(self, on):
        if on:
            self.ambience = plus.createSound("Sounds/elec_ambience_loop.wav", False, (0, 0, 0))
            plus.loopSound(self.ambience)
            
            self.RegisterZone("Center Zone", 1)
            self.RegisterZone("Center Zone1", 4)
            self.RegisterZone("Center Zone2", 5)
            self.electricity = Hazards.Electricity((.016, -.818, .001))
            self.AddHazard(self.electricity)
            
            self.RegisterZone("Button Zone 1", 2)
            self.RegisterZone("Button Zone 2", 3)
            
            # grid (in 'plus' shape)
            self.AddCollisionLine((6, 4), (6, -4))
            self.AddCollisionLine((6, -4), (3.6, -4))
            self.AddCollisionLine((3.6, -4), (3.6, -6.5))
            self.AddCollisionLine((3.6, -6.5), (-3.6, -6.5))
            self.AddCollisionLine((-3.6, -6.5), (-3.6, -4))
            self.AddCollisionLine((-3.6, -4), (-6, -4))
            self.AddCollisionLine((-6, -4), (-6, 4))
            self.AddCollisionLine((-6, 4), (-3.6, 4))
            self.AddCollisionLine((-3.5, 4), (-3.6, 6.5))
            self.AddCollisionLine((-3.6, 6.5), (3.6, 6.5))
            self.AddCollisionLine((3.6, 6.5), (3.6, 4))
            self.AddCollisionLine((3.6, 4), (6, 4))
            
            self.AddPOV(0, (0, 11), (1, 7))
            self.AddPOV(1, (8, 8), (2, 0))
            self.AddPOV(2, (10.5, 0), (3, 1))
            self.AddPOV(3, (8, -8), (4, 2))
            self.AddPOV(4, (0, -11), (5, 3))
            self.AddPOV(5, (-8, -8), (6, 4))
            self.AddPOV(6, (-10.5, 0), (7, 5))
            self.AddPOV(7, (-8, 8), (0, 6))
            
            self.CreateLightning(0, (-4, -2.2, 0), (0, -2.2, 0))
            self.CreateLightning(1, (0, -2.1, 0), (-4, -2.1, 0))
            self.CreateLightning(2, (-4, -2.0, 0), (0, -2.0, 0))
            self.CreateLightning(3, (0, -2.2, 3.4), (0, -2.2, 0))
            self.CreateLightning(4, (0, -2.1, 0), (0, -2.1, 3.4))
            self.CreateLightning(5, (0, -2.0, 3.4), (0, -2.0, 0))
            self.CreateLightning(6, (4, -2.2, 0), (0, -2.2, 0))
            self.CreateLightning(7, (0, -2.1, 0), (4, -2.1, 0))
            self.CreateLightning(8, (4, -2.0, 0), (0, -2.0, 0))
            self.CreateLightning(9, (0, -2.2, -3.4), (0, -2.2, 0))
            self.CreateLightning(10, (0, -2.1, 0), (0, -2.1, -3.4))
            self.CreateLightning(11, (0, -2.0, -3.4), (0, -2.0, 0))
            
            n = 0
            while n < 12:
                self.SetLightningVisible(n, True)
                n += 1

        # walls
        self.AddCollisionLine((16, 15.8), (16, -15.8))
        self.AddCollisionLine((16, -15.8), (11.8, -20))
        self.AddCollisionLine((11.8, -20), (-11.8, -20))
        self.AddCollisionLine((-11.8, -20), (-16, -15.8))
        self.AddCollisionLine((-16, -15.8), (-16, 15.8))
        self.AddCollisionLine((-16, 15.8), (-11.8, 20))
        self.AddCollisionLine((-11.8, 20), (11.8, 20))
        self.AddCollisionLine((11.8, 20), (16, 15.8))
        
        return Arenas.SuperArena.HazardsOn(self, on)
        
    def Tick(self):
        # do our stuff here
        if self.bHazardsOn:
            self.electricity.Tick()
            
            if self.zaptimer > 0:
                self.zaptimer -= .25
                if self.zaptimer <= 0:
                    self.SetAllLightningVisible(False)
                    self.ResetLightningPositions()
            
            if self.chargetimer > 0.0:
                self.chargetimer -= .25
                if self.chargetimer <= 0.0:
                    self.SetLightningVisible(0, True)
                    self.SetLightningVisible(1, True)
                    self.SetLightningVisible(2, True)
                    self.chargetimer = 0.0
                elif self.chargetimer <= 1.25:
                    self.SetLightningVisible(3, True)
                    self.SetLightningVisible(4, True)
                    self.SetLightningVisible(5, True)
                elif self.chargetimer <= 2.5:
                    self.SetLightningVisible(6, True)
                    self.SetLightningVisible(7, True)
                    self.SetLightningVisible(8, True)
                elif self.chargetimer <= 3.75:
                    self.SetLightningVisible(9, True)
                    self.SetLightningVisible(10, True)
                    self.SetLightningVisible(11, True)
        
        return Arenas.SuperArena.Tick(self)
        
    def ZoneEvent(self, direction, id, robot, chassis):
        if id==1:
            self.electricity.ZoneEvent(direction, robot, chassis)
        elif id==2 and direction==1:
            self.electricity.Button()
        elif id==3 and direction==1:
            self.electricity.Button()
        elif id==4:
            self.electricity.ZoneEvent(direction, robot, chassis)
        elif id==5:
            self.electricity.ZoneEvent(direction, robot, chassis)
            
        return True
        
    def Charge(self, time, bots):
        self.chargetimer = time
        self.zaptimer = .5
        self.SetAllLightningVisible(False)
        
        n = 0
        for bot, in_range in bots.iteritems():
            if in_range:
                self.SetLightningStartEnd(n, (0, -2.2, 0), plus.getLocation(bot))
                self.SetLightningStartEnd(n+1, plus.getLocation(bot), (0, -2.1, 0))
                self.SetLightningStartEnd(n+2, (0, -2.0, 0), plus.getLocation(bot))
                self.SetLightningVisible(n, True)
                self.SetLightningVisible(n+1, True)
                self.SetLightningVisible(n+2, True)
                n+=3
            
    def ResetLightningPositions(self):
        self.SetLightningStartEnd(0, (-4, -2.2, 0), (0, -2.2, 0))
        self.SetLightningStartEnd(1, (0, -2.1, 0), (-4, -2.1, 0))
        self.SetLightningStartEnd(2, (-4, -2.0, 0), (0, -2.0, 0))
        self.SetLightningStartEnd(3, (0, -2.2, 3.4), (0, -2.2, 0))
        self.SetLightningStartEnd(4, (0, -2.1, 0), (0, -2.1, 3.4))
        self.SetLightningStartEnd(5, (0, -2.0, 3.4), (0, -2.0, 0))
        self.SetLightningStartEnd(6, (4, -2.2, 0), (0, -2.2, 0))
        self.SetLightningStartEnd(7, (0, -2.1, 0), (4, -2.1, 0))
        self.SetLightningStartEnd(8, (4, -2.0, 0), (0, -2.0, 0))
        self.SetLightningStartEnd(9, (0, -2.2, -3.4), (0, -2.2, 0))
        self.SetLightningStartEnd(10, (0, -2.1, 0), (0, -2.1, -3.4))
        self.SetLightningStartEnd(11, (0, -2.0, -3.4), (0, -2.0, 0))
    
    def SetAllLightningVisible(self, bVisible):
        for n in range(12):
            self.SetLightningVisible(n, bVisible)
            
Arenas.register(ElectricArena)
