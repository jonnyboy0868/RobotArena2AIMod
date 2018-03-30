from __future__ import generators
import plus
import Arenas
import Hazards
import random

class KingOfHill(Arenas.SuperArena):
    def __init__(self, filename, scoring_zone_name, scoring_zone_id, scoring_zone_loc):
        Arenas.SuperArena.__init__(self, filename)
        
        self.initial_scoring_delay = 0
        self.scoring_delay = 0
        self.king_of_hill = False
        self.scoring_zone_name = scoring_zone_name
        self.scoring_zone_id = scoring_zone_id
        self.scoring_zone_loc = scoring_zone_loc
        self.scoringPlayer = None
        self.scoresound = plus.createSound("Sounds\\start_scoring.wav", True, (0, 0, 0))
        
    def __del__(self):
        plus.removeSound(self.scoresound)
        Arenas.SuperArena.__del__(self)

    def Activate(self, on):
        if on:
            self.king_of_hill = (plus.getGameType() == "KING OF THE HILL")
        
        Arenas.SuperArena.Activate(self, on)
       
    def Tick(self):
        # I'M KING OF THE HILL! (score 10 pts every 1 second after initial 3 second delay)
        initial_delay = 0
        scoring_delay = .5
        points = 10
        
        if self.king_of_hill and not plus.isMatchOver():
            king = self.OneTrueKing()
            if king != None:
                if self.initial_scoring_delay >= initial_delay:
                    self.scoring_delay += self.tickInterval
                    while self.scoring_delay > scoring_delay:
                        self.scoringPlayer = king - 1
                        plus.playSound(self.scoresound)
                        plus.addPoints(self.scoringPlayer, points)
                        self.scoring_delay -= scoring_delay
                else:
                    self.initial_scoring_delay += self.tickInterval
            else:
                self.initial_scoring_delay = 0
                self.scoring_delay = 0
                self.scoringPlayer = None
        
        return Arenas.SuperArena.Tick(self)

    def OneTrueKing(self):
        robots = self.GetRobotsInPhantom(self.scoring_zone_name)
        x = [robot for robot in robots if not plus.isDefeated(robot - 1)]
        if len(x) == 1: return x[0]
        else: return None
        
    def GetScoringPlayer(self):
        return self.scoringPlayer

    def GetScoringLocation(self):
        return self.scoring_zone_loc
        
class KingArena(KingOfHill):
    "In the LumaZone King of the Hill arena, the central point zone is surrounded by sharp teeth-like hazards."
    name = "LumaZone"
    preview = "kingofhill/king_preview.bmp"
    game_types = ['KING OF THE HILL']
    extent = (-14, 14, 15, -15)

    def __init__(self):
        KingOfHill.__init__(self, "Arenas/kingofhill/king.gmf", "kingzone", 5, (0, 0, 0))
        plus.setBackColor(0,0,0)
        self.teeth = []
        
        fov = 0.015
        self.AddStaticCamera("Static cam 1", (13.3, 8.22, -21.67), (0.262,-0.55), 66*fov)
        self.AddStaticCamera("Static cam 2", (-11.16, 9.18, 0), (0.652, 1.572), 56*fov)
        self.AddWatchCamera("Watch cam 1", (-11.18, 3.9, -2.34), (6,15, 65*fov, 40*fov))
        self.AddWatchCamera("Watch cam 1", (-1.16, 6.9, -16.06), (2,10, 75*fov, 45*fov))

        #self.RegisterZone("kingzone", 5)

    def AddShadowReceivers(self):
        self.SetShadowSource(-8.921, 12.265, -9.938)
        
        #Arena Shadow Triangles
        self.AddShadowTriangle((-14.5696,0.119301,-11.1481), (-14.5762,0.119301,10.8661), (-14.5696,2.82762,-11.1481))
        self.AddShadowTriangle((-14.5696,2.82762,-11.1481), (-14.5762,0.119301,10.8661), (-14.5762,2.82762,10.8661))
        self.AddShadowTriangle((-11.0168,0.119301,-14.7009), (-14.5696,0.119301,-11.1481), (-11.0168,2.82762,-14.7009))
        self.AddShadowTriangle((-11.0168,2.82762,-14.7009), (-14.5696,0.119301,-11.1481), (-14.5696,2.82762,-11.1481))
        self.AddShadowTriangle((11.0104,0.119301,-14.6943), (-11.0168,0.119301,-14.7009), (11.0104,2.82762,-14.6943))
        self.AddShadowTriangle((11.0104,2.82762,-14.6943), (-11.0168,0.119301,-14.7009), (-11.0168,2.82762,-14.7009))
        self.AddShadowTriangle((14.5546,0.119301,-11.1468), (11.0104,0.119301,-14.6943), (14.5546,2.82762,-11.1468))
        self.AddShadowTriangle((14.5546,2.82762,-11.1468), (11.0104,0.119301,-14.6943), (11.0104,2.82762,-14.6943))
        self.AddShadowTriangle((14.5551,0.119301,10.8721), (14.5546,0.119301,-11.1468), (14.5551,2.82762,10.8721))
        self.AddShadowTriangle((14.5551,2.82762,10.8721), (14.5546,0.119301,-11.1468), (14.5546,2.82762,-11.1468))
        self.AddShadowTriangle((11.0043,0.119301,14.4203), (14.5551,0.119301,10.8721), (11.0043,2.82762,14.4203))
        self.AddShadowTriangle((11.0043,2.82762,14.4203), (14.5551,0.119301,10.8721), (14.5551,2.82762,10.8721))
        self.AddShadowTriangle((-10.9964,0.119301,14.4192), (11.0043,0.119301,14.4203), (-10.9964,2.82762,14.4192))
        self.AddShadowTriangle((-10.9964,2.82762,14.4192), (11.0043,0.119301,14.4203), (11.0043,2.82762,14.4203))
        self.AddShadowTriangle((-14.5762,0.119301,10.8661), (-10.9964,0.119301,14.4192), (-14.5762,2.82762,10.8661))
        self.AddShadowTriangle((-14.5762,2.82762,10.8661), (-10.9964,0.119301,14.4192), (-10.9964,2.82762,14.4192))
        self.AddShadowTriangle((-14.5696,0.119301,-11.1481), (-10.9964,0.119301,14.4192), (-14.5762,0.119301,10.8661))
        self.AddShadowTriangle((-14.5696,0.119301,-11.1481), (-11.0168,0.119301,-14.7009), (-10.9964,0.119301,14.4192))
        self.AddShadowTriangle((-11.0168,0.119301,-14.7009), (11.0043,0.119301,14.4203), (-10.9964,0.119301,14.4192))
        self.AddShadowTriangle((11.0104,0.119301,-14.6943), (11.0043,0.119301,14.4203), (-11.0168,0.119301,-14.7009))
        self.AddShadowTriangle((14.5546,0.119301,-11.1468), (11.0043,0.119301,14.4203), (11.0104,0.119301,-14.6943))
        self.AddShadowTriangle((14.5551,0.119301,10.8721), (11.0043,0.119301,14.4203), (14.5546,0.119301,-11.1468))
        self.AddShadowTriangle((-5.00001,0.116127,-4.99964), (-5.00001,0.116127,5.00038), (5.00001,0.116127,5.00038))
        self.AddShadowTriangle((5.00001,0.116127,5.00038), (5.00001,0.116127,-4.99964), (-5.00001,0.116127,-4.99964))
        self.AddShadowTriangle((-2.28311,0.668198,-2.28274), (2.28311,0.668198,-2.28274), (2.28311,0.668198,2.28348))
        self.AddShadowTriangle((2.28311,0.668198,2.28348), (-2.28311,0.668198,2.28348), (-2.28311,0.668198,-2.28274))
        self.AddShadowTriangle((-5.00001,0.116127,-4.99964), (5.00001,0.116127,-4.99964), (2.28311,0.668198,-2.28274))
        self.AddShadowTriangle((2.28311,0.668198,-2.28274), (-2.28311,0.668198,-2.28274), (-5.00001,0.116127,-4.99964))
        self.AddShadowTriangle((5.00001,0.116127,-4.99964), (5.00001,0.116127,5.00038), (2.28311,0.668198,2.28348))
        self.AddShadowTriangle((2.28311,0.668198,2.28348), (2.28311,0.668198,-2.28274), (5.00001,0.116127,-4.99964))
        self.AddShadowTriangle((5.00001,0.116127,5.00038), (-5.00001,0.116127,5.00038), (-2.28311,0.668198,2.28348))
        self.AddShadowTriangle((-2.28311,0.668198,2.28348), (2.28311,0.668198,2.28348), (5.00001,0.116127,5.00038))
        self.AddShadowTriangle((-5.00001,0.116127,5.00038), (-5.00001,0.116127,-4.99964), (-2.28311,0.668198,-2.28274))
        self.AddShadowTriangle((-2.28311,0.668198,-2.28274), (-2.28311,0.668198,2.28348), (-5.00001,0.116127,5.00038))
        
    def HazardsOn(self, on):
        if on:
            prism = self.AddPrismatic("arena_collision", "teeth01", -0.432429,0.791208,0.432429, 0, 1.1, 0)
            self.teeth.append(Hazards.Spikes(prism, 40000, (5.85, 0, -5.87)))
            prism = self.AddPrismatic("arena_collision", "teeth02", 0.470183,0.746898,-0.470183, 0, 1.1, 0)
            self.teeth.append(Hazards.Spikes(prism, 40000, (-5.91, 0, 5.93)))
            prism = self.AddPrismatic("arena_collision", "teeth03", 0.470183,0.746898,0.470183, 0, 1.1, 0)
            self.teeth.append(Hazards.Spikes(prism, 40000, (-5.91, 0, -5.87)))
            prism = self.AddPrismatic("arena_collision", "teeth04", -0.444467,0.777752,-0.444467, 0, 1.1, 0)
            self.teeth.append(Hazards.Spikes(prism, 40000, (5.85, 0, 5.93)))
            
            for hazard in self.teeth:
                self.AddHazard(hazard)
            
            self.SetSubMaterialSound("teeth01", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("teeth02", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("teeth03", "metal", .7, "Sounds\\hzd_spike_hit.wav")
            self.SetSubMaterialSound("teeth04", "metal", .7, "Sounds\\hzd_spike_hit.wav")
        
            self.RegisterZone("hazardzone01", 1)
            self.RegisterZone("hazardzone02", 2)
            self.RegisterZone("hazardzone03", 3)
            self.RegisterZone("hazardzone04", 4)
            
            self.AddCollisionLine((-7.8, 6.8), (-6.8, 7.8))
            self.AddCollisionLine((-6.8, 7.8), (-4, 5))
            self.AddCollisionLine((-4, 5), (-5, 4))
            self.AddCollisionLine((-5, 4), (-7.8, 6.8))
            
            self.AddCollisionLine((4, 5), (6.8, 7.8))
            self.AddCollisionLine((6.8, 7.8), (7.8, 6.8))
            self.AddCollisionLine((7.8, 6.8), (5, 4))
            self.AddCollisionLine((5, 4), (4, 5))
            
            self.AddCollisionLine((3.9, -5), (4.9, -3.9))
            self.AddCollisionLine((4.9, -3.9), (7.8, -6.8))
            self.AddCollisionLine((7.8, -6.8), (6.8, -7.8))
            self.AddCollisionLine((6.8, -7.8), (3.9, -5))
            
            self.AddCollisionLine((-7.8, -6.8), (-5, -4))
            self.AddCollisionLine((-5, -4), (-4, -5))
            self.AddCollisionLine((-4, -5), (-6.8, -7.8))
            self.AddCollisionLine((-6.8, -7.8), (-7.8, -6.8))
            
            self.AddPOV(0, (0, 11), (1, 7, 8))
            self.AddPOV(1, (10, 10), (0, 2))
            self.AddPOV(2, (11, 0), (1, 3, 8))
            self.AddPOV(3, (10, -10), (2, 4))
            self.AddPOV(4, (0, -11), (3, 5, 8))
            self.AddPOV(5, (-10, -10), (4, 6))
            self.AddPOV(6, (-11, 0), (5, 7, 8))
            self.AddPOV(7, (-10, 10), (0, 6))
            self.AddPOV(8, (0, 0), (0, 2, 4, 6))

        # walls
        self.AddCollisionLine((14.7, 10.8), (11.1, 14.4))
        self.AddCollisionLine((11.1, 14.4), (-11.1, 14.4))
        self.AddCollisionLine((-11.1, 14.4), (-14.7, 10.8))
        self.AddCollisionLine((-14.7, 10.8), (-14.7, -11.1))
        self.AddCollisionLine((-14.7, -11.1), (-11.1, -14.7))
        self.AddCollisionLine((-11.1, -14.7), (11.1, -14.7))
        self.AddCollisionLine((11.1, -14.7), (14.7, -11.1))
        self.AddCollisionLine((14.7, -11.1), (14.7, 10.8))
        
        return Arenas.SuperArena.HazardsOn(self, on)

    def Introduction(self):
        sounds = self.intro_sounds

        # set initial camera & fade from black
        plus.setCameraPosition(2.47282,4.90546,-21.0784)
        plus.setCameraRotation(0.189584,-0.106736)
        plus.setCameraFOV(0.675)
        plus.fadeFromBlack(.25)

        #start playing music loop
        self.intro_music = plus.createSound("Sounds/intro_music/tool_rage.wav", False, (0,0,0))
        plus.setVolume(self.intro_music, 0, 0)
        plus.loopSound(self.intro_music)
        yield .25
        
        #load all sounds now to decrease lag later
        sounds['crowd'] = plus.createSound("Sounds/crowd/LoudCheer_Loop.wav", False, (0,0,0))
        
        arenaOpt = ("Sounds/announcers/Arena_Lumazone_Welcome.wav", "Sounds/announcers/Arena_Lumazone_Enter.wav")
        sounds['arena'] = plus.createSound(random.choice(arenaOpt), False, (0,0,0))
        genericOpt = ("Intro_Hilltop_AreYouWorthyToBeKing.wav", "Arena_NowhereToHide.wav", "Intro_TheFansAreReady.wav", "Intro_GreatMatchComingYourWay.wav", "Intro_FansAreRestless.wav", "Intro_PerfectEveningForDestruction.wav", "Intro_HoldOnToYourSeats.wav", "Misc_CrowdOnEdge.wav")
        sounds['generic'] = plus.createSound("Sounds/announcers/"+random.choice(genericOpt), False, (0,0,0))
        hazardOpt = ("Sounds/announcers/Hazard_Lumazone_WatchOutRazorSharpTeeth.wav", "Sounds/announcers/Hazard_Clawtop_AvoidRazorSharpClaws.wav")
        sounds['hazards'] = plus.createSound(random.choice(hazardOpt), False, (0,0,0))
        botOpt = ("Bots_YouCanFeelTension.wav", "Bots_ColdChill.wav", "Bots_FansLoveTheseBots.wav", "Bots_SeeingInterestingDesigns.wav", "Bots_CrowdPoisedBotsArmed.wav")
        sounds['bots'] = plus.createSound("Sounds/announcers/"+random.choice(botOpt), False, (0,0,0))
        
        #intro cam, welcom comment
        plus.playSound(sounds['arena'])
        plus.fadeInToLoop(sounds['crowd'], -100, 800)
        plus.animateCamera((2.47282,4.90546,-21.0784), (0.189584,-0.106736), 0.675, (-22.9376,16.2378,19.3794), (0.46936,2.27133), 0.675, 0, 8)
        yield 2
        plus.fadeOutLoop(sounds['crowd'], 8000)
        yield 1
        
        #play a generic (or specific) secondary comment
        plus.playSound(sounds['generic'])
        yield 5
        
        #hazard cams
        if self.bHazardsOn:
            plus.playSound(sounds['hazards'])
            plus.animateCamera((-4.82442,5.71925,-1.69162), (0.398397,0.953306), 0.675, (0.555657,5.71925,7.11452), (0.780508,1.73408), 0.675, 0, 3)
            plus.animateCamera((10.417,14.0656,-0.0584636), (0.905459,-1.5708), 0.675, (7.69244,7.70235,-0.0584633), (0.72887,-1.5708), 0.675, 3, 6)
            yield 6

        players = plus.getPlayers()
        pcount = len(players)
        if pcount>0: plus.playSound(sounds['bots'])
        delaytime = 6 - pcount
        
        if 0 in players:
            #bot 1 cam
            plus.animateCamera((-2.60866,0.740549,9.78314), (0.106223,-1.62101), 0.675, (-6.23971,3.38917,5.81047), (0.604615,-0.739469), 0.675, 0, delaytime)
            yield delaytime

        if 1 in players:
            #bot 2 cam
            plus.animateCamera((4.86175,1.37137,-10.2102), (0.268659,1.5411), 0.675, (7.12714,2.65029,-6.89398), (0.56599,2.43338), 0.675, 0, delaytime)
            yield delaytime
            
        if 2 in players:
            #bot 3 cam
            plus.animateCamera((4.64171,1.37931,10.3059), (0.260425,1.71269), 0.675, (6.14093,2.66505,5.91269), (0.47737,0.7804), 0.675, 0, delaytime)
            yield delaytime
            
        if 3 in players:
            #bot 4 cam
            plus.animateCamera((-4.65238,1.18389,-9.96377), (0.205875,-1.5708), 0.675, (-7.36988,2.09448,-7.132), (0.473249,-2.33549), 0.675, 0, delaytime)
            yield delaytime
            
        #fade out music
        plus.fadeOutLoop(self.intro_music, 2000)
        yield 2
        
        # done
        yield 0
 
    def Tick(self):
        # do our stuff here
        if self.bHazardsOn:
            for t in self.teeth: t.Tick()
        
        return KingOfHill.Tick(self)
        
    def ZoneEvent(self, direction, id, robot, chassis):
        if id>0 and id < 5: self.teeth[id-1].ZoneEvent(direction)
        
        return True

Arenas.register(KingArena)
