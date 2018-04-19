from __future__ import generators
import plus
import Arenas
import Hazards
import random

class SkullArena(Arenas.SuperArena):
    "Originally a set for a horror movie about metallic skeletons, you'll find a giant metal skull laughing at your bot as it falls into the deathpit or is hit by the spike hazards."
    name = "Metal Skull"
    preview = "skull/dm_skull_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-15.0, 7.5, 16.0, -23.5)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/skull/skull.gmf")
        plus.setBackColor(0, 0, 0)
        
        prism = self.AddPrismatic("structure_collision", "grate", -0.446198, 0, -0.894934, 0, 5, 0)
        self.grate = Hazards.PitSlider(prism, 45, (-4.46, -3.9, -16.83))
        self.AddHazard(self.grate)
        self.grate.slider.SetPowerSettings(.3, -400) #overriding default power setting
        
        fov = 0.015
        self.AddStaticCamera("Static Cam 1", (16.39, 8.34, -7.88), (0.47, -1.45), 74*fov)
        self.AddStaticCamera("Static Cam 2", (0.54, 23.73, -6.96), (1.57, 0), 78*fov)
        self.AddWatchCamera("Watch Cam 1", (-1.26, 3.0, 4.56), (2,8, 80*fov, 60*fov))
        self.AddWatchCamera("Watch Cam 2", (4.87, 12.87, -0.94), (18,20,65*fov,30*fov))
        self.AddWatchCamera("Watch Cam 3", (4.4, 5.59, -10.47), (4,12, 70*fov,50*fov))

        self.players = ()

    def AddShadowReceivers(self):
        self.SetShadowSource(9.272, 12, -3.649)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((2.23731,-0.405113,-16.0715), (-7.92283,-0.405113,-10.9914), (-6.9965,-0.397824,-12.5564))
        self.AddShadowTriangle((-6.9965,-0.397824,-12.5564), (0.428135,-0.397824,-16.2687), (2.23731,-0.405113,-16.0715))
        self.AddShadowTriangle((-7.92283,-0.405113,-10.9914), (-11.0871,-0.405113,-17.5295), (-9.30872,-0.397824,-17.3342))
        self.AddShadowTriangle((-9.30872,-0.397824,-17.3342), (-6.9965,-0.397824,-12.5564), (-7.92283,-0.405113,-10.9914))
        self.AddShadowTriangle((-11.0871,-0.405113,-17.5295), (-1.08429,-0.405113,-22.6191), (-1.999,-0.397824,-21.0535))
        self.AddShadowTriangle((-1.999,-0.397824,-21.0535), (-9.30872,-0.397824,-17.3342), (-11.0871,-0.405113,-17.5295))
        self.AddShadowTriangle((-1.08429,-0.405113,-22.6191), (2.23731,-0.405113,-16.0715), (0.428135,-0.397824,-16.2687))
        self.AddShadowTriangle((0.428135,-0.397824,-16.2687), (-1.999,-0.397824,-21.0535), (-1.08429,-0.405113,-22.6191))
        self.AddShadowTriangle((7.31707,-0.405113,1.70845), (-2.83992,-0.405113,6.78883), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((2.23765,-0.405113,-10.8005), (7.31707,-0.405113,1.70845), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((2.23765,-0.405113,-10.8005), (7.32151,-0.405113,-10.8), (7.31707,-0.405113,1.70845))
        self.AddShadowTriangle((-7.92283,-0.405113,-10.9914), (2.23731,-0.405113,-16.0715), (2.23765,-0.405113,-10.8005))
        self.AddShadowTriangle((-7.92283,-0.405113,-10.9914), (2.23765,-0.405113,-10.8005), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((-7.92269,-0.405113,1.51781), (-7.92283,-0.405113,-10.9914), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((-15.5427,1.05211,-10.9913), (-7.92283,1.05211,-10.9914), (-7.92269,1.05211,1.51781))
        self.AddShadowTriangle((-7.92269,1.05211,1.51781), (-15.5427,1.05211,6.78853), (-15.5427,1.05211,-10.9913))
        self.AddShadowTriangle((-7.92283,-0.405113,-10.9914), (-7.92269,-0.405113,1.51781), (-7.92269,1.05211,1.51781))
        self.AddShadowTriangle((-7.92269,1.05211,1.51781), (-7.92283,1.05211,-10.9914), (-7.92283,-0.405113,-10.9914))
        self.AddShadowTriangle((-2.83882,-0.405113,1.51823), (-2.83992,-0.405113,6.78883), (-7.32579,1.05211,6.78853))
        self.AddShadowTriangle((-7.32579,1.05211,6.78853), (-7.32579,1.05211,1.51781), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((-7.32579,1.05211,6.78853), (-7.92269,1.05211,1.51781), (-7.32579,1.05211,1.51781))
        self.AddShadowTriangle((-7.92269,1.05211,1.51781), (-7.32579,1.05211,6.78853), (-15.5427,1.05211,6.78853))
        self.AddShadowTriangle((-7.32579,1.05211,1.51781), (-7.92269,-0.405113,1.51781), (-2.83882,-0.405113,1.51823))
        self.AddShadowTriangle((-7.92269,-0.405113,1.51781), (-7.32579,1.05211,1.51781), (-7.92269,1.05211,1.51781))
        self.AddShadowTriangle((14.9414,1.05205,1.70878), (7.31707,1.05211,1.70844), (7.32151,1.05211,-10.8))
        self.AddShadowTriangle((7.32151,1.05211,-10.8), (14.9417,1.05205,-16.0711), (14.9414,1.05205,1.70878))
        self.AddShadowTriangle((7.31707,-0.405113,1.70845), (7.32151,-0.405113,-10.8), (7.32151,1.05211,-10.8))
        self.AddShadowTriangle((7.32151,1.05211,-10.8), (7.31707,1.05211,1.70844), (7.31707,-0.405113,1.70845))
        self.AddShadowTriangle((2.23765,-0.405113,-10.8005), (2.23731,-0.405113,-16.0715), (6.72461,1.05211,-16.0708))
        self.AddShadowTriangle((6.72461,1.05211,-16.0708), (6.72461,1.05211,-10.8), (2.23765,-0.405113,-10.8005))
        self.AddShadowTriangle((6.72461,1.05211,-16.0708), (7.32151,1.05211,-10.8), (6.72461,1.05211,-10.8))
        self.AddShadowTriangle((7.32151,1.05211,-10.8), (6.72461,1.05211,-16.0708), (14.9417,1.05205,-16.0711))
        self.AddShadowTriangle((6.72461,1.05211,-10.8), (7.32151,-0.405113,-10.8), (2.23765,-0.405113,-10.8005))
        self.AddShadowTriangle((7.32151,-0.405113,-10.8), (6.72461,1.05211,-10.8), (7.32151,1.05211,-10.8))
        self.AddShadowTriangle((7.31707,-0.405113,1.70845), (7.31707,1.05211,1.70844), (-2.83992,-0.405113,6.78883))
        self.AddShadowTriangle((-15.5532,10.0043,-11.0028), (-7.93328,10.0043,-11.0029), (-7.92283,1.05211,-10.9914))
        self.AddShadowTriangle((-7.92283,1.05211,-10.9914), (-15.5427,1.05211,-10.9913), (-15.5532,10.0043,-11.0028))
        self.AddShadowTriangle((-15.5532,10.0043,6.77708), (-15.5532,10.0043,-11.0028), (-15.5427,1.05211,-10.9913))
        self.AddShadowTriangle((-15.5427,1.05211,-10.9913), (-15.5427,1.05211,6.78853), (-15.5532,10.0043,6.77708))
        self.AddShadowTriangle((-7.32579,1.05211,6.78853), (-2.83992,-0.405113,6.78883), (-2.85037,10.0043,6.77738))
        self.AddShadowTriangle((-7.32579,1.05211,6.78853), (-15.5532,10.0043,6.77708), (-15.5427,1.05211,6.78853))
        self.AddShadowTriangle((-15.5532,10.0043,6.77708), (-7.32579,1.05211,6.78853), (-2.85037,10.0043,6.77738))
        self.AddShadowTriangle((14.931,10.0043,1.69733), (7.30662,10.0043,1.69698), (7.31707,1.05211,1.70844))
        self.AddShadowTriangle((7.31707,1.05211,1.70844), (14.9414,1.05205,1.70878), (14.931,10.0043,1.69733))
        self.AddShadowTriangle((14.9313,10.0043,-16.0826), (14.931,10.0043,1.69733), (14.9414,1.05205,1.70878))
        self.AddShadowTriangle((14.9414,1.05205,1.70878), (14.9417,1.05205,-16.0711), (14.9313,10.0043,-16.0826))
        self.AddShadowTriangle((6.72461,1.05211,-16.0708), (2.23731,-0.405113,-16.0715), (2.22686,10.0043,-16.0829))
        self.AddShadowTriangle((6.72461,1.05211,-16.0708), (14.9313,10.0043,-16.0826), (14.9417,1.05205,-16.0711))
        self.AddShadowTriangle((14.9313,10.0043,-16.0826), (6.72461,1.05211,-16.0708), (2.22686,10.0043,-16.0829))
        self.AddShadowTriangle((7.30662,10.0043,1.69698), (-2.85037,10.0043,6.77738), (-2.83992,-0.405113,6.78883))
        self.AddShadowTriangle((-2.83992,-0.405113,6.78883), (7.31707,1.05211,1.70844), (7.30662,10.0043,1.69698))
        
    def Activate(self, on):
        if on: self.players = plus.getPlayers()
        
        Arenas.SuperArena.Activate(self, on)

    def HazardsOn(self, on):
        if on:
            prism = self.AddPrismatic("structure_collision", "spikes1", 0, 1, 0, 0, .8, 0)
            self.spikes1 = Hazards.Spikes(prism, 40000, (5.90, -0.5, -4.73))
            self.AddHazard(self.spikes1)
            prism = self.AddPrismatic("structure_collision", "spikes2", 0, 1, 0, 0, .8, 0)
            self.spikes2 = Hazards.Spikes(prism, 40000, (3.28, -0.5, 2.01))
            self.AddHazard(self.spikes2)
            
            self.SetSubMaterial("spikes1", "metal", .7)
            self.SetSubMaterial("spikes2", "metal", .7)
        
            self.grate.setactive(True)
            #self.RegisterZone("deathzone", 1)
            self.RegisterZone("spike_zone1", 2)
            self.RegisterZone("spike_zone2", 3)
            
            self.AddCollisionLine((2.3, 3.4), (1.6, 2))
            self.AddCollisionLine((1.6, 2), (4.2, .7))
            self.AddCollisionLine((4.2, .7), (4.9, 2))
            
            self.AddCollisionLine((6.7, -6.2), (5.1, -6.2))
            self.AddCollisionLine((5.1, -6.2), (5.1, -3.3))
            self.AddCollisionLine((5.1, -3.3), (6.7, -3.3))
            
            self.AddCollisionLine((.4, -16.3), (-7, -12.5))
        else:
            self.grate.setactive(False)

        # walls
        self.AddCollisionLine((14.9, 1.7), (7.3, 1.7))
        self.AddCollisionLine((7.3, 1.7), (-2.8, 6.7))
        self.AddCollisionLine((-2.8, 6.7), (-15.5, 6.7))
        self.AddCollisionLine((-15.5, 6.7), (-15.5, -11))
        self.AddCollisionLine((-15.5, -11), (-7.9, -11))
        self.AddCollisionLine((-7.9, -11), (-11.1, -17.5))
        self.AddCollisionLine((-11.1, -17.5), (-1, -22.6))
        self.AddCollisionLine((-1, -22.6), (2.2, -16))
        self.AddCollisionLine((2.2, -16), (14.9, -16))
        self.AddCollisionLine((14.9, -16), (14.9, 1.7))
        
        # edges
        self.AddCollisionLine((-7.9, -11), (-7.9, 1.5))
        self.AddCollisionLine((-7.9, 1.5), (-2.8, 1.5))
        
        self.AddCollisionLine((2.2, -10.8), (7.3, -10.8))
        self.AddCollisionLine((7.3, -10.8), (7.3, 1.7))
        
        self.AddPOV(0, (10.5, -13.5), (1,))
        self.AddPOV(1, (-.5, -13), (0, 2))
        self.AddPOV(2, (-1.6, -8), (1, 3))
        self.AddPOV(3, (-.5, -1), (2, 4))
        self.AddPOV(4, (-1.5, 3), (3, 5))
        self.AddPOV(5, (-12, 4), (4,))

        return Arenas.SuperArena.HazardsOn(self, on)

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-14.4853,15.1727,13.3798)
        plus.setCameraRotation(0.457532,-3.48619)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/tool_rage.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Skull_Enter.wav", "Sounds/announcers/Arena_Skull_Welcome.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Arena_NowhereToHide.wav", "Intro_Skull_MostWorthyUnscathed.wav", "Intro_Skull_NotAvoidGazeFromSkull.wav", "Intro_Skull_NotToAngerRestlessSpirits.wav", "Intro_Skull_WatchOutForHypnoticStare.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Skull_CantSurviveDeathPit.wav", "Sounds/announcers/Hazard_Skull_PainDescribesDeathPit.wav", "Sounds/announcers/Hazard_Skull_SpikesDontPitWill.wav", "Sounds/announcers/Hazard_Skull_SpikesWillMakeQuickWork.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-14.4853,15.1727,13.3798), (0.457532,-3.48619), 0.675, (17.857,15.1727,1.92684), (0.381297,-2.24567), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-2.47876,10.7013,-4.98399), (0.903606,1.56699), 0.675, (2.75409,4.05801,-4.96409), (0.903606,1.56699), 0.675, 0, 3)
            plus.animateCamera((1.37991,6.8947,-4.88167), (0.0,-2.6764), 0.675, (-0.231112,5.18265,-8.09135), (0.444853,-2.6764), 0.675, 3, 6)
            yield 6

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((3.39245,9.03134,-8.04641), (0.645966,0.879583), 0.675, (11.0903,3.49325,-8.08438), (0.316493,0.0227453), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((-4.58458,8.62153,-0.59323), (0.632534,-2.30769), 0.675, (-11.6613,3.12554,-0.593229), (0.259727,-3.10167), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((3.95237,4.09431,-4.94451), (0.241217,2.38952), 0.675, (3.18309,2.23979,-13.3437), (0.0998337,1.51592), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-3.35515,5.93161,-2.57273), (0.462884,-1.09528), 0.675, (-6.49374,2.4358,3.58492), (0.227729,-1.8789), 0.675, 0, delaytime)
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
            self.grate.Tick()

        # check to see if anyone has been "eliminated" by falling off the tabletop
        for each in self.players:
            if plus.getLocation(each)[1] < -2:
                plus.eliminatePlayer(each)

        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        if id == 1: death = True # this id is not in use
        elif id == 2: self.spikes1.ZoneEvent(direction)
        elif id == 3: self.spikes2.ZoneEvent(direction)
        
        return True

Arenas.register(SkullArena)
