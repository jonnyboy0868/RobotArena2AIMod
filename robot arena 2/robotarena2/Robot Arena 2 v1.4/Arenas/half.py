from __future__ import generators
import plus
import Arenas
import Hazards
import random

class HalfCircleArena(Arenas.SuperArena):
    "Watch out for the massive hammer!  It will crush your bot like a little tin can."
    name = "Half Circle Arena"
    preview = "half/dm_half_circle_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-17, 17, 4, -18)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/half/half.gmf")
        self.total = 0
        plus.setBackColor(0,0,0)
        
        # Static Cameras
        self.AddStaticCamera("Overhead", (-17.8, 39, 0), (1.21, 1.575), 0.675)
        self.AddStaticCamera("Side 1", (-34.5, 21.3, 12.25), (0.5085, 1.932), 0.675)
        self.AddStaticCamera("Side 2", (-34.5, 21.3, -12.25), (0.5085, 1.225), 0.675)
        
        # Watch Cameras
        self.AddWatchCamera("Skybox", (2.5, 6.6, 0), (5, 30, 0.975, 0.675))
        self.AddWatchCamera("Pole 1", (-13.6, 9.9, -11.4), (5, 30, 0.675, 0.675))
        self.AddWatchCamera("Pole 2", (-13.6, 9.9, 11.4), (5, 30, 0.675, 0.675))
        
    def __del__(self):
        Arenas.SuperArena.__del__(self)
        
    def AddShadowReceivers(self):
        self.SetShadowSource(-12.834, 10, -7.507)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((-8.908,0.0542354,2.67294), (-3.09372,0.0542354,10.2955), (-13.6478,0.0542354,11.4519))
        self.AddShadowTriangle((-16.7416,0.0542354,6.09343), (-8.908,0.0542354,2.67294), (-13.6478,0.0542354,11.4519))
        self.AddShadowTriangle((-17.816,0.0542354,-3.15277e-006), (-8.908,0.0542354,-2.69838), (-8.908,0.0542354,2.67294))
        self.AddShadowTriangle((-13.6478,0.0542354,-11.4519), (-8.908,0.0542354,-15.4291), (-3.09371,0.0542354,-10.3344))
        self.AddShadowTriangle((-17.816,0.0542354,-3.15277e-006), (-8.908,0.0542354,2.67294), (-16.7416,0.0542354,6.09343))
        self.AddShadowTriangle((-13.6478,0.0542354,-11.4519), (-8.908,0.0542354,-2.69838), (-16.7416,0.0542354,-6.09343))
        self.AddShadowTriangle((-16.7416,0.0542354,-6.09343), (-8.908,0.0542354,-2.69838), (-17.816,0.0542354,-3.15277e-006))
        self.AddShadowTriangle((-3.09372,0.0542354,10.2955), (3.09372,0.0542354,10.2955), (3.09372,0.0542354,17.5453))
        self.AddShadowTriangle((3.09372,0.0542354,17.5453), (-3.09372,0.0542354,17.5453), (-3.09372,0.0542354,10.2955))
        self.AddShadowTriangle((-3.09371,-1.6896,3.32284), (3.09372,-1.6896,3.32284), (3.09372,0.0542354,10.2955))
        self.AddShadowTriangle((3.09372,0.0542354,10.2955), (-3.09372,0.0542354,10.2955), (-3.09371,-1.6896,3.32284))
        self.AddShadowTriangle((-3.09371,0.0542354,-17.5453), (3.09372,0.0542354,-17.5453), (3.09372,0.0542354,-10.3344))
        self.AddShadowTriangle((3.09372,0.0542354,-10.3344), (-3.09371,0.0542354,-10.3344), (-3.09371,0.0542354,-17.5453))
        self.AddShadowTriangle((3.09372,-1.6896,-3.34541), (-3.09371,-1.6896,3.32284), (-3.09371,-1.6896,-3.34541))
        self.AddShadowTriangle((-3.09371,0.0542354,-10.3344), (3.09372,0.0542354,-10.3344), (3.09372,-1.6896,-3.34541))
        self.AddShadowTriangle((3.09372,-1.6896,-3.34541), (-3.09371,-1.6896,-3.34541), (-3.09371,0.0542354,-10.3344))
        self.AddShadowTriangle((-8.908,0.0542354,-15.4291), (-3.09371,0.0542354,-17.5453), (-3.09371,0.0542354,-10.3344))
        self.AddShadowTriangle((-8.908,0.0542354,-2.69838), (-3.09371,0.0542354,-10.3344), (-3.09371,0.0542354,-3.34541))
        self.AddShadowTriangle((-13.6478,0.0542354,-11.4519), (-3.09371,0.0542354,-10.3344), (-8.908,0.0542354,-2.69838))
        self.AddShadowTriangle((-3.74085,-1.6896,-2.69828), (-3.74086,-1.6896,2.67539), (-8.908,0.0542354,2.67294))
        self.AddShadowTriangle((-8.908,0.0542354,2.67294), (-8.908,0.0542354,-2.69838), (-3.74085,-1.6896,-2.69828))
        self.AddShadowTriangle((-8.908,0.0542354,15.4291), (-3.09372,0.0542354,10.2955), (-3.09372,0.0542354,17.5453))
        self.AddShadowTriangle((-3.09372,0.0542354,10.2955), (-8.908,0.0542354,15.4291), (-13.6478,0.0542354,11.4519))
        self.AddShadowTriangle((-3.09371,0.0542354,3.32284), (-3.09372,0.0542354,10.2955), (-8.908,0.0542354,2.67294))
        self.AddShadowTriangle((-3.74085,0.0542354,-2.69828), (-8.908,0.0542354,-2.69838), (-3.09371,0.0542354,-3.34541))
        self.AddShadowTriangle((-3.09371,-1.6896,-3.34541), (-3.09371,-1.6896,3.32284), (-3.74086,-1.6896,2.67539))
        self.AddShadowTriangle((-3.74085,0.0542354,2.67539), (-3.09371,0.0542354,3.32284), (-8.908,0.0542354,2.67294))
        self.AddShadowTriangle((-3.74086,-1.6896,2.67539), (-3.74085,-1.6896,-2.69828), (-3.09371,-1.6896,-3.34541))
        self.AddShadowTriangle((-3.09371,-1.6896,3.32284), (3.09372,-1.6896,-3.34541), (3.09372,-1.6896,3.32284))
        
    def HazardsOn(self, on):
        if on:
            prism = self.AddPrismatic("Collision Box", "Killsaws 1", 0, 1, 0, 0, .36, 0)
            self.saw1 = Hazards.Saws(prism, (-6.81, 0, -11.86))
            self.AddHazard(self.saw1)
            prism = self.AddPrismatic("Collision Box", "Killsaws 2", 0, 1, 0, 0, .36, 0)
            self.saw2 = Hazards.Saws(prism, (-6.81, 0, 12.0))
            self.AddHazard(self.saw2)
        
            hinge = self.GetHinge("Hinge01")
            self.RegisterZone("Hammer Zone", 1)
            self.Hammer1 = Hazards.Hammer(hinge)
            self.AddHazard(self.Hammer1)
            self.RegisterZone("Killsaw 1 Zone", 2)
            self.RegisterZone("Killsaw 2 Zone", 3)
            self.SetSubMaterialSound("Spike1_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike2_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike3_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike4_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike5_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike6_Zone", "metal", .8, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterial("Killsaw 1 Zone", "metal", .8)
            self.SetSubMaterial("Killsaw 2 Zone", "metal", .8)
            self.SetSubMaterialSound("Killsaws 1", "metal", .8, "Sounds\\sawblade_hits_loop.wav")
            self.SetSubMaterialSound("Killsaws 2", "metal", .8, "Sounds\\sawblade_hits_loop.wav")
            self.SetSubMaterialSound("Hammer", "metal", .8, "Sounds\\hzd_hammer_thud.wav")
            
            # saw 1 avoidance
            self.AddCollisionLine((-7.4, 12.3), (-7, 12.7))
            self.AddCollisionLine((-7, 12.7), (-6.2, 11.6))
            self.AddCollisionLine((-6.2, 11.6), (-6.6, 11.2))
            self.AddCollisionLine((-6.6, 11.2), (-7.4, 12.3))
            
            # hammer avoidance
            self.AddCollisionLine((0, .5), (1.2, .5))
            self.AddCollisionLine((0, .5), (0, -.5))
            self.AddCollisionLine((0, -.5), (1.2, -.5))
            
            # saw 2 avoidance
            self.AddCollisionLine((-6.6, -11.1), (-6.2, -11.5))
            self.AddCollisionLine((-6.2, -11.5), (-7, -12.6))
            self.AddCollisionLine((-7, -12.6), (-7.4, -12.3))
            self.AddCollisionLine((-7.4, -12.3), (-6.6, -11.1))
            
        self.AddCollisionLine((-3.1, 10.3), (-3.1, 2.7))
        self.AddCollisionLine((-3.1, 2.7), (-8.9, 2.7))
        
        self.AddCollisionLine((-8.9, -2.7), (-3.1, -2.7))
        self.AddCollisionLine((-3.1, -2.7), (-3.1, -10.3))
        
        # walls
        self.AddCollisionLine((3, 17.5), (-3, 17.5))
        self.AddCollisionLine((-3, 17.5), (-8.9, 15.4))
        self.AddCollisionLine((-8.9, 15.4), (-13.6, 11.5))
        self.AddCollisionLine((-13.6, 11.5), (-16.7, 6.1))
        self.AddCollisionLine((-16.7, 6.1), (-17.8, 0))
        self.AddCollisionLine((-17.8, 0), (-16.7, -6.1))
        self.AddCollisionLine((-16.7, -6.1), (-13.6, -11.5))
        self.AddCollisionLine((-13.6, -11.5), (-8.9, -15.4))
        self.AddCollisionLine((-8.9, -15.4), (-3, -17.5))
        self.AddCollisionLine((-3, -17.5), (3, -17.5))
        self.AddCollisionLine((3, -17.5), (3, 17.5))
        
        self.AddPOV(0, (0, 15), (1, 7, 8))
        self.AddPOV(1, (-1.5, 3.2), (0, 9))
        self.AddPOV(2, (-1.5, -3.2), (3, 9))
        self.AddPOV(3, (0, -15), (2, 4, 5))
        self.AddPOV(4, (-4.8, -11), (3, 11))
        self.AddPOV(5, (-8, -14), (3, 11))
        self.AddPOV(6, (-13.5, 0), (9, 10, 11))
        self.AddPOV(7, (-4.8, -11), (0, 10))
        self.AddPOV(8, (-8, 14), (0, 10))
        self.AddPOV(9, (-2, 0), (1, 2, 6))
        self.AddPOV(10, (-12.5, 7.5), (6, 7, 8))
        self.AddPOV(11, (-13, -7.5), (4, 5, 6))
        
        return Arenas.SuperArena.HazardsOn(self, on)
        
    def ZoneEvent(self, direction, id, robot, chassis):
        if (id==1):
            self.Hammer1.ZoneEvent(direction)
        elif (id==2):
            self.saw1.ZoneEvent(direction)
        elif (id==3):
            self.saw2.ZoneEvent(direction)
        return True

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-19.4933,16.3084,-32.4896)
        plus.setCameraRotation(0.408103,0.546509)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/whatgame_loop.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Half_HalfCircleEnter.wav", "Sounds/announcers/Arena_Half_Enter.wav", "Sounds/announcers/Arena_Half_HammerWelcome.wav", "Sounds/announcers/Arena_Half_Welcome.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Half_AvoidHammerAtAllCost.wav", "Sounds/announcers/Hazard_Half_GiantHammerHeadache.wav", "Sounds/announcers/Hazard_Half_HammerBestIfAvoided.wav", "Sounds/announcers/Hazard_Half_WatchOutForTheGiantHammer.wav", "Sounds/announcers/Hazard_Half_WatchOutHammerLong.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-19.4933,16.3084,-32.4896), (0.408103,0.546509), 0.675, (-14.7027,7.61579,20.5245), (0.289939,2.52256), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-10.9991,8.66534,0.0246233), (0.536457,1.57113), 0.675, (-7.18447,2.54641,-7.08777), (0.0932602,0.855399), 0.675, 0, 6.5)
            #plus.animateCamera((-2.58287,8.69154,6.695), (0.917142,-0.676867), 0.675, (-4.18791,2.15696,8.69258), (0.484794,-0.676868), 0.675, 4, 5.5)
            yield 6.5

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-0.0135928,2.81498,8.94584), (0.364223,0.00518426), 0.675, (5.6259,2.81498,12.0027), (0.352851,-1.05747), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((0.038355,2.48803,-8.86167), (0.314693,3.14159), 0.675, (-4.99442,5.15277,-12.0717), (0.746794,2.11357), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((-7.09289,5.34361,10.3559), (0.649647,-1.99906), 0.675, (-7.79949,1.41688,3.68885), (0.151466,-0.917292), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-8.50312,1.86428,-4.64377), (0.257124,-2.12405), 0.675, (-12.6077,5.05862,-1.10308), (0.623381,-3.05371), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
 
    def Tick(self):
        # do our stuff here
        if self.bHazardsOn:
            self.Hammer1.Tick()
        return Arenas.SuperArena.Tick(self)

Arenas.register(HalfCircleArena)
