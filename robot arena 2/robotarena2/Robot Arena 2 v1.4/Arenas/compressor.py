from __future__ import generators
import plus
import Arenas
import Hazards
import random

class CompressorArena(Arenas.SuperArena):
    "Be cautious of the side areas.  Getting caught in there could be a tight squeeze!"
    name = "Compressor Arena"
    preview = "compressor/dm_compressor_preview.bmp"
    game_types = ['DEATHMATCH', 'BATTLE ROYAL', 'TEAM MATCH']
    extent = (-20, 17, 21, -18)

    def __init__(self):
        Arenas.SuperArena.__init__(self, "Arenas/compressor/compressor.gmf")
        plus.setBackColor(0,0,0)
        
        # Static Cameras
        self.AddStaticCamera("Overhead", (0, 45.0, 0), (1.5708, 3.1415), 0.8164)
        self.AddStaticCamera("Side", (-30.0, 30.275, 0.5), (0.7158, 1.575), 0.675)
        self.AddStaticCamera("End", (0, 40.0, -27.0), (0.945, 0), 0.675)
        
        # Watch Cameras
        self.AddWatchCamera("Watch 1", (10.0, 13.05, 3.312), (1.0, 50.0, 0.75, 0.75))
        self.AddWatchCamera("Watch 2", (-10.0, 13.05, 3.312), (0.5, 50.0, 1.0, 0.175))
        
    def AddShadowReceivers(self):
        self.SetShadowSource(0.257, 13.418, 0.319)
        
        #Arena Floor Shadow Triangles
        self.AddShadowTriangle((-5.001,0.0923628,16.5595), (-6.16567,0.0923628,3.35045), (6.30246,0.0923628,3.35045))
        self.AddShadowTriangle((6.30246,0.0923628,-3.29042), (5.001,0.0923628,-16.4101), (8.80249,0.0923628,-16.4101))
        self.AddShadowTriangle((6.30246,0.0923628,-3.29042), (-4.9995,0.0923628,-16.4101), (5.001,0.0923628,-16.4101))
        self.AddShadowTriangle((5.001,0.0923628,-16.4101), (-4.9995,0.0923628,-16.4101), (5.001,0.0923635,-21.4004))
        self.AddShadowTriangle((-4.9995,0.0923635,-21.4004), (5.001,0.0923635,-21.4004), (-4.9995,0.0923628,-16.4101))
        self.AddShadowTriangle((-5.001,0.0923628,16.5595), (4.9995,0.0923628,16.5595), (-5.001,0.0923628,21.5986))
        self.AddShadowTriangle((4.9995,0.0923628,21.5986), (-5.001,0.0923628,21.5986), (4.9995,0.0923628,16.5595))
        self.AddShadowTriangle((4.9995,0.0923628,16.5595), (6.30246,0.0923628,3.35045), (8.80249,0.0923628,16.5595))
        self.AddShadowTriangle((6.30246,0.0923628,3.35045), (-6.16567,0.0923628,3.35045), (6.30246,0.0923628,-3.29042))
        self.AddShadowTriangle((4.9995,0.0923628,16.5595), (-5.001,0.0923628,16.5595), (6.30246,0.0923628,3.35045))
        self.AddShadowTriangle((13.8025,0.0923628,11.5595), (6.30246,0.0923628,3.35045), (13.8025,0.0923628,3.35045))
        self.AddShadowTriangle((8.80249,0.0923628,16.5595), (6.30246,0.0923628,3.35045), (13.8025,0.0923628,11.5595))
        self.AddShadowTriangle((13.8025,0.0923628,-11.4101), (13.8025,0.0923628,-3.29042), (6.30246,0.0923628,-3.29042))
        self.AddShadowTriangle((6.30246,0.0923628,-3.29042), (8.80249,0.0923628,-16.4101), (13.8025,0.0923628,-11.4101))
        self.AddShadowTriangle((13.8025,2.5983,-3.29042), (13.8025,2.5983,3.35045), (6.30246,0.0923628,3.35045))
        self.AddShadowTriangle((13.8025,2.5983,-3.29042), (6.30246,0.0923628,3.35045), (6.30246,0.0923628,-3.29042))
        self.AddShadowTriangle((13.8025,2.5983,3.35045), (13.8025,2.5983,-3.29042), (20.0978,2.5983,-3.29042))
        self.AddShadowTriangle((20.0978,2.5983,-3.29042), (20.0978,2.5983,3.35045), (13.8025,2.5983,3.35045))
        self.AddShadowTriangle((20.0978,2.5983,-3.29042), (13.8025,2.5983,-3.29042), (14.042,5.04499,-11.2716))
        self.AddShadowTriangle((14.042,5.04499,-11.2716), (20.0978,5.04499,-11.2716), (20.0978,2.5983,-3.29042))
        self.AddShadowTriangle((13.8025,2.5983,3.35045), (20.0978,2.5983,3.35045), (20.0978,5.04499,11.3316))
        self.AddShadowTriangle((20.0978,5.04499,11.3316), (14.042,5.04499,11.3316), (13.8025,2.5983,3.35045))
        self.AddShadowTriangle((14.042,5.04499,11.3316), (20.0978,5.04499,11.3316), (20.0978,5.04499,17.617))
        self.AddShadowTriangle((20.0978,5.04499,17.617), (14.042,5.04499,17.617), (14.042,5.04499,11.3316))
        self.AddShadowTriangle((20.0978,5.04499,-11.2716), (14.042,5.04499,-11.2716), (14.042,5.04499,-17.557))
        self.AddShadowTriangle((14.042,5.04499,-17.557), (20.0978,5.04499,-17.557), (20.0978,5.04499,-11.2716))
        self.AddShadowTriangle((-13.6657,0.0923628,11.5595), (-13.6657,0.0923628,3.35045), (-6.16567,0.0923628,3.35045))
        self.AddShadowTriangle((-8.6657,0.0923628,16.5595), (-13.6657,0.0923628,11.5595), (-6.16567,0.0923628,3.35045))
        self.AddShadowTriangle((-13.6657,0.0923628,-11.4101), (-8.6657,0.0923628,-16.4101), (-6.16567,0.0923628,-3.29042))
        self.AddShadowTriangle((-6.16567,0.0923628,-3.29042), (-13.6657,0.0923628,-3.29042), (-13.6657,0.0923628,-11.4101))
        self.AddShadowTriangle((-13.6657,2.5983,-3.29042), (-6.16567,0.0923628,3.35045), (-13.6657,2.5983,3.35045))
        self.AddShadowTriangle((-13.6657,2.5983,-3.29042), (-6.16567,0.0923628,-3.29042), (-6.16567,0.0923628,3.35045))
        self.AddShadowTriangle((-13.6657,2.5983,3.35045), (-19.9611,2.5983,-3.29042), (-13.6657,2.5983,-3.29042))
        self.AddShadowTriangle((-19.9611,2.5983,-3.29042), (-13.6657,2.5983,3.35045), (-19.9611,2.5983,3.35045))
        self.AddShadowTriangle((-19.9611,2.5983,-3.29042), (-13.9052,5.04499,-11.2716), (-13.6657,2.5983,-3.29042))
        self.AddShadowTriangle((-13.9052,5.04499,-11.2716), (-19.9611,2.5983,-3.29042), (-19.9611,5.04499,-11.2716))
        self.AddShadowTriangle((-13.6657,2.5983,3.35045), (-19.9611,5.04499,11.3316), (-19.9611,2.5983,3.35045))
        self.AddShadowTriangle((-19.9611,5.04499,11.3316), (-13.6657,2.5983,3.35045), (-13.9052,5.04499,11.3316))
        self.AddShadowTriangle((-13.9052,5.04499,11.3316), (-19.9611,5.04499,17.617), (-19.9611,5.04499,11.3316))
        self.AddShadowTriangle((-19.9611,5.04499,17.617), (-13.9052,5.04499,11.3316), (-13.9052,5.04499,17.617))
        self.AddShadowTriangle((-19.9611,5.04499,-11.2716), (-13.9052,5.04499,-17.557), (-13.9052,5.04499,-11.2716))
        self.AddShadowTriangle((-13.9052,5.04499,-17.557), (-19.9611,5.04499,-11.2716), (-19.9611,5.04499,-17.557))
        self.AddShadowTriangle((-8.6657,0.0923628,16.5595), (-6.16567,0.0923628,3.35045), (-5.001,0.0923628,16.5595))
        self.AddShadowTriangle((-8.6657,0.0923628,-16.4101), (-4.9995,0.0923628,-16.4101), (-6.16567,0.0923628,-3.29042))
        self.AddShadowTriangle((-4.9995,0.0923628,-16.4101), (6.30246,0.0923628,-3.29042), (-6.16567,0.0923628,-3.29042))
        self.AddShadowTriangle((-6.16567,0.0923628,3.35045), (-6.16567,0.0923628,-3.29042), (6.30246,0.0923628,-3.29042))
        
    def HazardsOn(self, on):
        if on:
            # Arena Hazards set to damage rubber
            self.SetSubMaterialSound("Spike1_Zone", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike2_Zone", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike3_Zone", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Spike4_Zone", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("Smash Arm LeftA", "metal", .9, "Sounds\\hzd_comp_hit.wav")
            self.SetSubMaterialSound("Smash Arm LeftB", "metal", .9, "Sounds\\hzd_comp_hit.wav")
            self.SetSubMaterialSound("Smash Arm RightA", "metal", .9, "Sounds\\hzd_comp_hit.wav")
            self.SetSubMaterialSound("Smash Arm RightB", "metal", .9, "Sounds\\hzd_comp_hit.wav")
        
            self.RegisterZone("Zone_1", 1)
            self.RegisterZone("Zone_2", 2)
            hingeA = self.GetHinge("Hinge02")
            hingeB = self.GetHinge("Hinge01")
            self.Smasher1 = Hazards.Smasher(hingeA, hingeB, (0, 0, 18.8))
            self.AddHazard(self.Smasher1)
            hingeA = self.GetHinge("Hinge03")
            hingeB = self.GetHinge("Hinge04")
            self.Smasher2 = Hazards.Smasher(hingeA, hingeB, (0, 0, -18.8))
            self.AddHazard(self.Smasher2)
            
            # top & bottom (to seal off hazards)
            self.AddCollisionLine((-20, 17.6), (20, 17.6))
            self.AddCollisionLine((20, -17.5), (-20, -17.5))
        else:
            # top & bottom (with hazards open)
            self.AddCollisionLine((-20, 17.6), (-5, 16.6))
            self.AddCollisionLine((5, 16.6), (20, 17.6))
            self.AddCollisionLine((-20, -17.6), (-5, -16.4))
            self.AddCollisionLine((5, -16.4), (20, -17.6))

        self.AddCollisionLine((-20, 17.6), (-20, -17.5))
        self.AddCollisionLine((20, 17.6), (20, -17.5))
        self.AddCollisionLine((-13.9, 17.6), (-14, 3.3))
        self.AddCollisionLine((-13.9, 3.3), (-6, 3.3))
        self.AddCollisionLine((6, 3.3), (14, 3.3))
        self.AddCollisionLine((14, 3.3), (14, 17.6))
        self.AddCollisionLine((-13.9, -3.3), (-14, -17.5))
        self.AddCollisionLine((-13.9, -3.3), (-6, -3.3))
        self.AddCollisionLine((6, -3.3), (14, -3))
        self.AddCollisionLine((14, -3.3), (14, -17.5))
        
        self.AddPOV(0, (-17, 0), (1,))
        self.AddPOV(1, (-4, 0), (0, 2, 3, 4, 5, 6)) 
        self.AddPOV(2, (-4, 6), (1, 4, 5, 6))
        self.AddPOV(3, (-4, -6), (1, 4, 5, 6))
        self.AddPOV(4, (4, 0), (1, 2, 3, 5, 6, 7))
        self.AddPOV(5, (4, 6), (1, 2, 3, 4))
        self.AddPOV(6, (4, -6), (1, 2, 3, 4))
        self.AddPOV(7, (18, 0), (4,))

        return Arenas.SuperArena.HazardsOn(self, on)
        
    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(-18.796,12.1984,-17.272)
        plus.setCameraRotation(0.423969,0.865228)
        plus.setCameraFOV(1.125)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/whatgame_loop.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Compressor_Welcome.wav", "Sounds/announcers/Arena_Compressor_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Compressor_ArenaHasLotsOfLove.wav", "Intro_Compressor_ArenaWillPutTheSqueezeOnYou.wav", "Intro_Compressor_HugsByThisArena.wav", "Intro_Compressor_OneStopWeightLoss.wav", "Intro_Compressor_WatchOutForSqueezePlay.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Compressor_ChanceToSqueezeOpponent.wav",)
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((-18.796,12.1984,-17.272), (0.423969,0.865228), 1.125, (-19.9251,12.1984,16.2866), (0.424582,2.20704), 1.125, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((13.7134,6.18017,3.63394), (0.290649,-0.719471), 0.675, (-7.77868,6.18017,7.07434), (0.404454,0.577052), 0.675, 0, 6)
            yield 6

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((17.2332,13.507,-0.465692), (0.460854,-0.00407328), 0.675, (17.2332,7.51223,4.56581), (0.154498,-0.00607065), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((-16.925,13.3559,0.0022261), (0.482615,-3.14159), 0.675, (-16.925,7.50829,-4.5782), (0.179304,-3.14159), 0.675, 0, delaytime)
            yield delaytime

        if 2 in players:
            #bot 3 cam
            plus.animateCamera((17.2675,13.3731,0.0045817), (0.484407,-3.14159), 0.675, (17.2675,7.48773,-4.54556), (0.177543,-3.14159), 0.675, 0, delaytime)
            yield delaytime

        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-16.9149,13.5552,-0.498395), (0.462194,0.0), 0.675, (-16.9149,7.50437,4.59265), (0.153293,0.0), 0.675, 0, delaytime)
            yield delaytime
        
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
 
    def Tick(self):
        if self.bHazardsOn:
            self.Smasher1.Tick()
            self.Smasher2.Tick()

        return Arenas.SuperArena.Tick(self)
        
    def ZoneEvent(self, direction, id, robot, chassis):
        #print "robot:", robot
        if id == 1:
            self.Smasher1.ZoneEvent(direction, robot)
        elif id == 2:
            self.Smasher2.ZoneEvent(direction, robot)
            
        return True

Arenas.register(CompressorArena)
