from __future__ import generators
import plus
import Arenas
import random
import math

class FlexTop(Arenas.SuperArena):
    "Not for the faint of heart, this arena has giant springs causing the table top to flex in all directions."
    name = "FlexTop"
    preview = "flextop/tts_preview.bmp"
    game_types = ['TABLETOP']
    extent = (-13, 13, 14, -14)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/flextop/flextop.gmf")
        self.total = 0
        plus.setBackColor(0,0,0)
        
        fmod = .015
        # static cameras
        #self.AddStaticCamera("Static 1", (-3.5, 9, -7.7), (math.pi / 6.0, 0), math.pi / 4.0)
        self.AddStaticCamera("Static 1", (-16.0, 16.0, -23.0), (.524, .576), fmod*49)
        self.AddStaticCamera("Static Cam 2", (0, 24.8, 0), (1.5708,0), 72*fmod)
        
        # watch camera
        #self.AddWatchCamera("Watch 1", (-12.1, 9.8, -11.7), (2.0, 20.0, math.pi / 3.5, math.pi / 9.0))
        self.AddWatchCamera("Watch 1", (-7.2, 10.4, -20.8), (2.0, 30.0, fmod*60, fmod*23))
        self.AddWatchCamera("Watch 2", (20.3, 17.1, -15.5), (2.0, 30.0, fmod*50, fmod*30))
        
        self.players = ()
        
    def Activate(self, on):
        if on: self.players = plus.getPlayers()
        
        Arenas.SuperArena.Activate(self, on)

    def HazardsOn(self, on):
        if on:
            self.hazardson = True
        else:
            self.hazardson = False
            self.SetPinned("floor_collision", True)
        
        self.AddCollisionLine((-2.5, -2.5), (-2.5, 2.5))
        self.AddCollisionLine((-2.5, 2.5), (2.5, 2.5))
        self.AddCollisionLine((2.5, 2.5), (2.5, -2.5))
        self.AddCollisionLine((2.5, -2.5), (-2.5, -2.5))
        
        self.AddPOV(0, (0, -7), (1, 7))
        self.AddPOV(1, (-5.2, -5.2), (0, 2))
        self.AddPOV(2, (-7, 0), (1, 3))
        self.AddPOV(3, (-5.2, 5.2), (2, 4))
        self.AddPOV(4, (0, 7), (3, 5))
        self.AddPOV(5, (5.2, 5.2), (4, 6))
        self.AddPOV(6, (7, 0), (5, 7))
        self.AddPOV(7, (5.2, -5.2), (0, 6))
        
        return Arenas.SuperArena.HazardsOn(self, on)

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(29.6377,34.3606,-29.1315)
        plus.setCameraRotation(0.690386,-0.790885)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/hopp_club.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Flextop_Welcome.wav", "Sounds/announcers/Arena_Flextop_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Flextop_YouWillNeedYourSeaLegs.wav", "Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Flextop_KeepingYourBalanceIsCritical.wav", "Sounds/announcers/Hazard_Flextop_ThrowOpponentOffBalance.wav", "Sounds/announcers/Hazard_Flextop_UseTheWeightOfYourBot.wav", "Sounds/announcers/Hazard_Flextop_WatchOutForTheHole.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((29.6377,34.3606,-29.1315), (0.690386,-0.790885), 0.675, (-29.1792,10.39,-12.9523), (0.31367,1.15033), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-17.6884,16.5919,-15.6043), (0.56934,0.844588), 0.675, (-6.83274,6.72283,-5.96326), (0.521594,0.844588), 0.675, 0, 4)
            yield 4

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((6.43971,3.87092,3.94558), (0.350625,-1.11641), 0.675, (0.0237769,2.93187,0.814993), (0.261509,-0.00240821), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((3.60867,2.37561,-2.2791), (0.162717,3.7282), 0.675, (-2.58717,3.33843,-2.2791), (0.32609,2.68668), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((-2.36166,3.05141,2.40419), (0.318849,-2.07566), 0.675, (-3.30958,2.08892,-2.17259), (0.20086,-1.133), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((2.94102,2.48805,-0.211806), (0.256925,1.5708), 0.675, (3.5538,3.70699,-3.41461), (0.444612,0.883552), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
        
    def AddShadowReceivers(self):
        #Shadow Light Sources
        self.SetShadowSource(0, 10, 0)
        
        # make the triangles move with the floor
        self.SetShadowPrimitive("floor_collision")
        
        floor = 1.15
        
        #Main Arena Shadow Triangles
        self.AddShadowTriangle((-5.48042e-007,floor,12.5377), (0.859148,floor,2.36049), (4.28816,floor,11.7816))
        self.AddShadowTriangle((-5.48042e-007,floor,12.5377), (0.0,floor,2.51198), (0.859148,floor,2.36049))
        self.AddShadowTriangle((4.28816,floor,11.7816), (1.61467,floor,1.92429), (8.0591,floor,9.60446))
        self.AddShadowTriangle((4.28816,floor,11.7816), (0.859148,floor,2.36049), (1.61467,floor,1.92429))
        self.AddShadowTriangle((8.0591,floor,9.60446), (2.17544,floor,1.25599), (10.858,floor,6.26887))
        self.AddShadowTriangle((8.0591,floor,9.60446), (1.61467,floor,1.92429), (2.17544,floor,1.25599))
        self.AddShadowTriangle((10.858,floor,6.26887), (2.47382,floor,0.436201), (12.3473,floor,2.17715))
        self.AddShadowTriangle((10.858,floor,6.26887), (2.17544,floor,1.25599), (2.47382,floor,0.436201))
        self.AddShadowTriangle((12.3473,floor,2.17715), (2.47382,floor,-0.436201), (12.3473,floor,-2.17716))
        self.AddShadowTriangle((12.3473,floor,2.17715), (2.47382,floor,0.436201), (2.47382,floor,-0.436201))
        self.AddShadowTriangle((12.3473,floor,-2.17716), (2.17544,floor,-1.25599), (10.858,floor,-6.26887))
        self.AddShadowTriangle((12.3473,floor,-2.17716), (2.47382,floor,-0.436201), (2.17544,floor,-1.25599))
        self.AddShadowTriangle((10.858,floor,-6.26887), (1.61467,floor,-1.92429), (8.0591,floor,-9.60446))
        self.AddShadowTriangle((10.858,floor,-6.26887), (2.17544,floor,-1.25599), (1.61467,floor,-1.92429))
        self.AddShadowTriangle((8.0591,floor,-9.60446), (0.859148,floor,-2.36049), (4.28816,floor,-11.7816))
        self.AddShadowTriangle((8.0591,floor,-9.60446), (1.61467,floor,-1.92429), (0.859148,floor,-2.36049))
        self.AddShadowTriangle((4.28816,floor,-11.7816), (-3.34391e-007,floor,-2.51198), (-1.669e-006,floor,-12.5377))
        self.AddShadowTriangle((4.28816,floor,-11.7816), (0.859148,floor,-2.36049), (-3.34391e-007,floor,-2.51198))
        self.AddShadowTriangle((-1.669e-006,floor,-12.5377), (-0.859149,floor,-2.36049), (-4.28816,floor,-11.7816))
        self.AddShadowTriangle((-1.669e-006,floor,-12.5377), (-3.34391e-007,floor,-2.51198), (-0.859149,floor,-2.36049))
        self.AddShadowTriangle((-4.28816,floor,-11.7816), (-1.61467,floor,-1.92429), (-8.0591,floor,-9.60446))
        self.AddShadowTriangle((-4.28816,floor,-11.7816), (-0.859149,floor,-2.36049), (-1.61467,floor,-1.92429))
        self.AddShadowTriangle((-8.0591,floor,-9.60446), (-2.17544,floor,-1.25599), (-10.858,floor,-6.26886))
        self.AddShadowTriangle((-8.0591,floor,-9.60446), (-1.61467,floor,-1.92429), (-2.17544,floor,-1.25599))
        self.AddShadowTriangle((-10.858,floor,-6.26886), (-2.47382,floor,-0.436201), (-12.3473,floor,-2.17715))
        self.AddShadowTriangle((-10.858,floor,-6.26886), (-2.17544,floor,-1.25599), (-2.47382,floor,-0.436201))
        self.AddShadowTriangle((-12.3473,floor,-2.17715), (-2.47382,floor,0.436202), (-12.3473,floor,2.17716))
        self.AddShadowTriangle((-12.3473,floor,-2.17715), (-2.47382,floor,-0.436201), (-2.47382,floor,0.436202))
        self.AddShadowTriangle((-12.3473,floor,2.17716), (-2.17544,floor,1.25599), (-10.858,floor,6.26887))
        self.AddShadowTriangle((-12.3473,floor,2.17716), (-2.47382,floor,0.436202), (-2.17544,floor,1.25599))
        self.AddShadowTriangle((-10.858,floor,6.26887), (-1.61467,floor,1.92429), (-8.0591,floor,9.60446))
        self.AddShadowTriangle((-10.858,floor,6.26887), (-2.17544,floor,1.25599), (-1.61467,floor,1.92429))
        self.AddShadowTriangle((-8.0591,floor,9.60446), (-0.859148,floor,2.36049), (-4.28815,floor,11.7816))
        self.AddShadowTriangle((-8.0591,floor,9.60446), (-1.61467,floor,1.92429), (-0.859148,floor,2.36049))
        self.AddShadowTriangle((-4.28815,floor,11.7816), (0.0,floor,2.51198), (-5.48042e-007,floor,12.5377))
        self.AddShadowTriangle((-4.28815,floor,11.7816), (-0.859148,floor,2.36049), (0.0,floor,2.51198))
                
    def Tick(self):
        # check to see if anyone has been "eliminated" by falling off the tabletop
        for each in self.players:
            if plus.getLocation(each)[1] < -6:
                plus.eliminatePlayer(each)

        return Arenas.SuperArena.Tick(self)

    def DistanceToEdge(self, location):
        # using a tabletop radius of 10.0
        distance = math.sqrt(location[0] * location[0] + location[2] * location[2])
        heading = math.atan2(location[0], location[2])
        return (10 - distance, distance >= 10, heading)

    def HeadingAwayFromEdge(self, location):
        dist, over, h = self.DistanceToEdge(location)
        
        return h + math.pi

    def IsStraightPathClear(self, start, end, ignore_hazards):
        # check to see if end point is off the top
        if end[0] * end[0] + end[2] * end[2] > 121: return False
        else: return Arenas.SuperArena.IsStraightPathClear(self, start, end, ignore_hazards)
        
Arenas.register(FlexTop)
