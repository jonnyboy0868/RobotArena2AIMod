from __future__ import generators
import plus
import Arenas
import Hazards
import random

import math

class BoxArena(Arenas.SuperArena):
    "The Combat Arena is a traditional square arena surrounded by high-impact polycarbonate glazing. Hazards include spikes and sawblades that rise from below the floor."
    name = "Combat Arena"
    preview = "box/box_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/box/boxarena.gmf")
        plus.setBackColor(0, 0, 0)
        
        fmod = .015
        # static cameras
        #self.AddStaticCamera("Static 1", (-3.5, 9, -7.7), (math.pi / 6.0, 0), math.pi / 4.0)
        self.AddStaticCamera("Static 1", (17.7, 11, -28.4), (.367, -.576), fmod*50)
        self.AddStaticCamera("Static 2", (0, 48, 0), (math.pi/2.01, 0), fmod*37)
        self.AddStaticCamera("Static 3", (0, 13, -26), (.524, 0), fmod*52)
        
        # watch camera
        #self.AddWatchCamera("Watch 1", (-12.1, 9.8, -11.7), (2.0, 20.0, math.pi / 3.5, math.pi / 9.0))
        self.AddWatchCamera("Watch 1", (-12.1, 7.0, -11.7), (2.0, 30.0, fmod*60, fmod*25))
        
    def AddShadowReceivers(self):
        #Shadow Light Sources
        self.SetShadowSource(0.653, 6.894, -0.418)
        
        #Main Arena Shadow Triangles
        self.AddShadowTriangle((-12.7,-2.1126,13.0027), (-12.7,-2.1126,-12.3973), (12.7,-2.1126,13.0027))
        self.AddShadowTriangle((12.7,-2.1126,-12.3973), (12.7,-2.1126,13.0027), (-12.7,-2.1126,-12.3973))
        self.AddShadowTriangle((12.7,-2.1126,-12.3973), (-12.7,-2.1126,-12.3973), (12.7,2.2245,-12.3973))
        self.AddShadowTriangle((-12.7,2.2245,-12.3973), (12.7,2.2245,-12.3973), (-12.7,-2.1126,-12.3973))
        self.AddShadowTriangle((12.7,-2.1126,13.0027), (12.7,-2.1126,-12.3973), (12.7,2.2245,13.0027))
        self.AddShadowTriangle((12.7,2.2245,-12.3973), (12.7,2.2245,13.0027), (12.7,-2.1126,-12.3973))
        self.AddShadowTriangle((-12.7,-2.1126,13.0027), (12.7,-2.1126,13.0027), (-12.7,2.2245,13.0027))
        self.AddShadowTriangle((12.7,2.2245,13.0027), (-12.7,2.2245,13.0027), (12.7,-2.1126,13.0027))
        self.AddShadowTriangle((-12.7,-2.1126,-12.3973), (-12.7,-2.1126,13.0027), (-12.7,2.2245,-12.3973))
        self.AddShadowTriangle((-12.7,2.2245,13.0027), (-12.7,2.2245,-12.3973), (-12.7,-2.1126,13.0027))
        
    def HazardsOn(self, on):
        if on:
            prism = self.AddPrismatic("arena_collision", "spikes1", 0, 1, 0, 0, .8, 0)
            self.spikes1 = Hazards.Spikes(prism, 40000, (-3.7, -2.2, -5.2))
            prism = self.AddPrismatic("arena_collision", "spikes2", 0, 1, 0, 0, .8, 0)
            self.spikes2 = Hazards.Spikes(prism, 40000, (4.9, -2.2, -5.2))
    
            prism = self.AddPrismatic("arena_collision", "floorsaw", 0, 1, 0, -.1, .46, 0)
            self.saw = Hazards.Saws(prism, (-.1, -2.2, 5.4))
    
            self.AddHazard(self.spikes1)
            self.AddHazard(self.spikes2)
            self.AddHazard(self.saw)
    
            self.SetSubMaterialSound("floorsaw", "metal", .8, "Sounds\\sawblade_hits_loop.wav")
            self.SetSubMaterialSound("spikes1", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("spikes2", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            
            self.RegisterZone("saw_zone", 1)
            self.RegisterZone("spike_zone1",2)
            self.RegisterZone("spike_zone2",3)
            
            # hazards
            self.AddCollisionLine((-1.6, 6.7), (1.3, 6.7))
            self.AddCollisionLine((1.3, 6.7), (1.3, 4))
            self.AddCollisionLine((1.3, 4), (-1.6, 4))
            self.AddCollisionLine((-1.6, 4), (-1.6, 6.7))
            
            self.AddCollisionLine((-4.4, -3.9), (-3, -3.9))
            self.AddCollisionLine((-3, -3.9), (-3, -6.3))
            self.AddCollisionLine((-3, -6.3), (-4.4, -6.3))
            self.AddCollisionLine((-4.4, -6.3), (-4.4, -3.9))
            
            self.AddCollisionLine((4.2, -3.9), (5.6, -3.9))
            self.AddCollisionLine((5.6, -3.9), (5.6, -6.4))
            self.AddCollisionLine((5.6, -6.4), (4.2, -6.4))
            self.AddCollisionLine((4.2, -6.4), (4.2, -3.9))

            self.AddPOV(0, (0, 10), (1, 3))
            self.AddPOV(1, (5, 5.5), (0, 2, 8))
            self.AddPOV(2, (0, 1), (1, 3, 4, 8, 5, 11))
            self.AddPOV(3, (-5, 5.5), (0, 2, 4))
            self.AddPOV(4, (-4, -1), (2, 3, 5, 7))
            self.AddPOV(5, (0, -5.3), (2, 4, 6, 11))
            self.AddPOV(6, (-4, -9), (5, 7, 10))
            self.AddPOV(7, (-7, -5.3), (4, 6))
            self.AddPOV(8, (5, -1), (1, 2, 9, 11))
            self.AddPOV(9, (8, -5.3), (8, 10))
            self.AddPOV(10, (5, -9), (6, 9, 11))
            self.AddPOV(11, (1.5, -5.3), (2, 8, 5, 10))
 
        else:
            # hazards should be in their "hidden" position
            pass
            
        # walls
        self.AddCollisionLine((-12.7, 13), (-12.7, -12.4))
        self.AddCollisionLine((-12.7, -12.4), (12.7, -12.4))
        self.AddCollisionLine((12.7, -12.4), (12.7, 13))
        self.AddCollisionLine((12.7, 13), (-12.7, 13))

        return Arenas.SuperArena.HazardsOn(self, on)

    def Activate(self, on):
        return Arenas.SuperArena.Activate(self, on)
        
    def Introduction(self):
        sounds = self.intro_sounds
        
        # set initial camera & fade from black
        plus.setCameraPosition(23.7554,14.3743,-47.141)
        plus.setCameraRotation(0.266024,-0.472956)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/smell_glue.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_CombatZone.wav", "Sounds/announcers/Arena_Combat_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Arena_Combat_CageOfSteel.wav", "Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_SawsSpikes.wav", "Sounds/announcers/Hazard_SawsSpikesFlesh.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((23.7554,14.3743,-47.141), (0.266024,-0.472956), 0.675, (30.3992,6.28651,8.97787), (0.193915,-1.86089), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((12.0623,13.9558,-10.831), (0.666964,-0.640974), 0.66, (12.0623,13.9558,-10.831), (0.666964,-0.640974), 0.24, 0, .5)
            plus.animateCamera((8.6126,4.07693,2.09747), (0.416206,-2.1045), 0.8862, (8.6126,4.07693,2.09747), (0.416206,-2.1045), 0.3162, 1, 1.5)
            yield 4

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-8.06563,1.12132,-3.88764), (0.210442,-0.141627), 0.8862, (-3.39987,1.12132,7.25815), (0.394558,-1.12997), 0.8862, 0, delaytime)
            yield delaytime
            
        if 1 in players:
            #bot 2 cam
            plus.animateCamera((5.22435,3.09861,-1.95753), (0.47197,2.53793), 0.8862, (4.59523,-0.911434,-5.42526), (0.147264,2.22609), 0.8862, 0, delaytime)
            yield delaytime
            
        if 2 in players:
            #bot 3 cam
            plus.animateCamera((5.59557,1.02128,2.1188), (0.294276,0.484751), 0.8862, (2.4611,1.02128,4.21063), (0.284205,0.877072), 0.5712, 0, delaytime)
            yield delaytime
            
        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-5.57326,2.86185,-4.16246), (0.612217,-2.45323), 0.825, (-4.44016,-0.507445,-5.44161), (0.203219,-2.19922), 0.825, 0, delaytime)
            yield delaytime
            
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
        
        
    def Tick(self):
        "Do our stuff here -- called every tickInterval seconds."
        
        if self.bHazardsOn:
            self.spikes1.Tick()
            self.spikes2.Tick()
            
        return Arenas.SuperArena.Tick(self)

    def ZoneEvent(self, direction, id, robot, chassis):
        #print "robot:", robot
        if id == 1:
            # entering or leaving saw zone
            self.saw.ZoneEvent(direction)
        elif id == 2:
            # entering spikes zone 1
            self.spikes1.ZoneEvent(direction)
        elif id == 3:
            #entering spike zone 2
            self.spikes2.ZoneEvent(direction)
            
        return True

Arenas.register(BoxArena)
