import plus
import random
from AI import vector3

import Arenas

class Hazard(object):
    def __init__(self, location):
        self.location = location
        
class Spikes(Hazard):
    
    def __init__(self, a_prismatic, a_power, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        #statuses: 0=waiting, 1=firing
        self.status = 0
        self.prismatic = a_prismatic
        self.power = a_power
        self.prismatic.SetAutoLock(False)
        self.timer = 0
        self.refcount = 0
        self.firesound = plus.createSound("Sounds\\hzd_spike_fire.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.firesound)
        
    def ZoneEvent(self, direction):
        if direction==1:
            self.timer = 0
            self.status = 1
            self.refcount += 1
        elif direction==-1:
            self.refcount -= 1
            if self.refcount == 0: self.status = 0
            
    def Tick(self):
        if self.status==1:
            self.timer += .5
            if self.timer == 1: self.FireTeeth()
            if self.timer == 2.5: self.timer = 0
            
    def FireTeeth(self):
        plus.playSound(self.firesound)
        self.prismatic.Lock(False)
        self.prismatic.ApplyForce(self.power)
        
class Saws(Hazard):

    def __init__(self, a_prismatic, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        #statuses: 0=off, 1=on
        self.status = 0
        self.prismatic = a_prismatic
        self.prismatic.SetAutoLock(False)
        self.prismatic.SetPowerSettings(2.0, -2000)
        self.timer = 0
        self.refcount = 0
        
    def ZoneEvent(self, direction):
        if direction==1:
            if self.refcount==0: self.MoveSaw(1)
            self.refcount += 1
        elif direction==-1:
            self.refcount -= 1
            if self.refcount==0: self.MoveSaw(-1)
            
    def MoveSaw(self, dir):
        self.prismatic.Lock(False)
        self.prismatic.SetDirection(dir)
        
        
class HellRaiser(Hazard):
    
    def __init__(self, a_hinge, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        #statuses: 0=waiting, 1=firing
        self.status = 0
        self.hinge = a_hinge
        self.hinge.SetAutoLocks(False, False)
        self.hinge.Lock(True)
        self.timer = 0
        self.soundHandle = plus.createSound("Sounds\\hellraiser_trigger.wav", 1, (0, 0, 0))
        
    def __del__(self):
        plus.removeSound(self.soundHandle)
        
    def Tick(self):
        self.timer += .5
        if (self.status == 1 and self.timer > 1):
            self.LowerHell()
                
    def RaiseHell(self):
        self.hinge.SetPowerSettings(80,1500)
        self.hinge.Lock(False)
        self.hinge.SetDirection(100)
        self.timer = 0
        self.status = 1
        plus.playSound(self.soundHandle)
        
    def LowerHell(self):
        self.hinge.SetPowerSettings(4, 200)
        self.hinge.Lock(False)
        self.hinge.SetDirection(-100)
        self.timer = 0
        self.status = 0
        
        
        
class PitSlider(Hazard):

    def __init__(self, a_prismatic, delay, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        self.slider = a_prismatic
        self.slider.SetPowerSettings(.2, 2000)
        self.slider.SetAutoLock(True)
        self.timer = 0
        self.slidetime = 0
        self.sliding = False
        self.delay = delay
        self.active = False
        self.slidesound = plus.createSound("Sounds\\hzd_trapfloor_loop.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.slidesound)
        
    def Tick(self):
        if self.active:
            self.timer += .5
            if self.timer == self.delay:
                self.slider.Lock(False)
                self.slider.SetDirection(1)
                self.active = False
                plus.loopSound(self.slidesound)
                self.sliding = True
                self.slidetime = 0
        
        if self.sliding:
            self.slidetime += .5
            if self.slidetime >= 16:
                plus.stopSound(self.slidesound)
            
    def setactive(self, state):
        self.active = state
        
class Hammer(Hazard):
    
    def __init__(self, a_hinge, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        #statuses: 0=waiting, 1=firing, 2=retracting to fire again, 3=retracting to shut down
        self.status = 0
        self.hinge = a_hinge
        self.hinge.SetAutoLocks(False, False)
        self.hinge.Lock(True)
        self.timer = 0
        self.refcount = 0
        self.firesound = plus.createSound("Sounds\\hzd_hammer_fire.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.firesound)
        
    def Tick(self):
        self.timer += .5
        if (self.status == 1 and self.timer > 1):
            self.Retract()
        if (self.status == 2 and self.timer > 2.5):
            self.Smash()
        if (self.status == 3 and self.timer > 3):
            self.Shutdown()
            
    def Smash(self):
        plus.playSound(self.firesound)
        self.hinge.SetPowerSettings(95,1200)
        self.hinge.Lock(False)
        self.hinge.SetDirection(100)
        self.timer = 0
        self.status = 1
        
    def Retract(self):
        self.hinge.SetPowerSettings(3, 300)
        self.hinge.Lock(False)
        self.hinge.SetDirection(-100)
        self.timer = 0
        self.status = 2
        
    def Shutdown(self):
        self.hinge.SetPowerSettings(0, 0)
        self.hinge.SetDirection(0)
        self.timer = 0
        self.status = 0
        
    def ZoneEvent(self, direction):
        if direction==1:
            if self.refcount==0: self.Smash()
            self.refcount += 1
        if direction==-1:
            self.refcount -= 1
            if self.refcount == 0:
                self.Retract()
                self.status = 3
                
class Smasher(Hazard):
    #used in Compressor Arena
    
    def __init__(self, a_hinge1, a_hinge2, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        #statuses: 0=waiting, 1=firing, 2=retracting to fire again, 3=retracting to shut down
        self.status = 0
        self.hinge1 = a_hinge1
        self.hinge1.SetAutoLocks(True, False)
        self.hinge1.Lock(True)
        self.hinge2 = a_hinge2
        self.hinge2.SetAutoLocks(True, False)
        self.hinge2.Lock(True)
        self.timer = 0
        self.refcount = 0
        self.Retract()
        self.status = 3
        self.firesound = plus.createSound("Sounds\\hzd_comp_fire.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.firesound)
        
    def Tick(self):
        self.timer += .5
        if (self.status == 1 and self.timer > 2):
            self.Retract()
        if (self.status == 2 and self.timer > 3):
            self.Smash()
        if (self.status == 3 and self.timer > 3):
            self.Shutdown()
            
    def Smash(self):
        plus.playSound(self.firesound)
        self.hinge1.SetPowerSettings(95, 15000)
        self.hinge1.Lock(False)
        self.hinge1.SetDirection(100)
        self.hinge2.SetPowerSettings(-95, 15000)
        self.hinge2.Lock(False)
        self.hinge2.SetDirection(100)
        self.timer = 0
        self.status = 1
        
    def Retract(self):
        self.hinge1.SetPowerSettings(12, 700)
        self.hinge1.Lock(False)
        self.hinge1.SetDirection(-100)
        self.hinge2.SetPowerSettings(-12, 700)
        self.hinge2.Lock(False)
        self.hinge2.SetDirection(-100)
        self.timer = 0
        self.status = 2
        
    def Shutdown(self):
        self.hinge1.SetPowerSettings(0, 0)
        self.hinge1.SetDirection(0)
        self.hinge2.SetPowerSettings(0, 0)
        self.hinge2.SetDirection(0)
        self.timer = 0
        self.status = 0
        
    def ZoneEvent(self, direction, robot):
        if direction==1:
            if self.refcount==0: self.Smash()
            self.refcount += 1
        if direction==-1:
            self.refcount -= 1
            if self.refcount == 0:
                self.Retract()
                self.status = 3
        
class TrapDoor(Hazard):

    def __init__(self, a_hinge, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        self.hinge = a_hinge
        self.hinge.Lock(True)
        self.ready = True
        self.firesound = plus.createSound("Sounds\\hzd_trapdoor.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.firesound)
        
    def Trigger(self):
        if self.ready:
            plus.playSound(self.firesound)
            self.hinge.Lock(False)
            self.hinge.SetDirection(100)
            self.hinge.ApplyTorque(300)
            self.ready = False
            return True
        else: return False
        
class Flame(Hazard):

    def __init__(self, location = (0, 0, 0), velocity = (0, 0, 0), variance = (0, 0, 0), yOffset = 0):
        Hazard.__init__(self, location)
        self.refcount = 0
        self.velocity = velocity
        self.variance = variance
        self.emitter = plus.AddParticleEmitter(self.location, self.velocity, self.variance)
        self.emitting = False
        self.timeEmitting = 0
        self.adjustedLoc = vector3(self.location)
        self.adjustedLoc.y += yOffset
        self.flamesound = plus.createSound("Sounds/flame_thrower.wav", True, self.location)
        
    def __del__(self):
        plus.removeSound(self.flamesound)
        
    def Tick(self):
        if self.emitting==True:
            if plus.isMatchOver():
                self.FlameOff()
                
            if self.timeEmitting<1:     #flames are long enough by the end of 1 second
                self.timeEmitting += .25
            
            vel = vector3(self.velocity)
            flamepos = vel * self.timeEmitting
            flamepos = flamepos + vector3(self.location)
            arena = Arenas.currentArena
            if arena:
                compinfo = plus.rayTest(self.adjustedLoc.asTuple(), flamepos.asTuple())
                if not compinfo[0]==-1:  # we got a valid bot and component back from the ray test
                    if not plus.isMatchPaused() and not plus.isMatchOver():
                        plus.damage(compinfo[0], compinfo[1], 25, (compinfo[2], compinfo[3], compinfo[4]))
    
    def FlameOff(self):
        self.emitter.SetEmitting(False)
        self.emitting = False
        plus.stopSound(self.flamesound)
    
    def FlameOn(self):
        self.emitter.SetEmitting(True)
        self.emitting = True
        plus.loopSound(self.flamesound)
        self.timeEmitting = 0
    
    def ZoneEvent(self, direction):
        if direction==1:
            self.refcount+= 1
            if self.refcount == 1:
                self.FlameOn()
        elif direction==-1:
            self.refcount -= 1
            if self.refcount == 0:
                self.FlameOff()
                
class Electricity(Hazard):

    def __init__(self, location = (0, 0, 0)):
        Hazard.__init__(self, location)
        self.chargetimer = 0.0
        self.zaptimer = 0.0
        #self.announcetimer = 12.0
        self.sensors = {}
        self.zapping = []
        self.zapsound = plus.createSound("Sounds/zap_loop.wav", True, self.location)
        self.chargesound = plus.createSound("Sounds/zap_charge2.wav", True, self.location)
        #self.announcer = (plus.createSound("Sounds/announcers/Misc_NowThatsAnEnergizer.wav", True, self.location), plus.createSound("Sounds/announcers/Misc_ShockingDisplayOfPower.wav", True, self.location), plus.createSound("Sounds/announcers/Misc_ThereGoesTheElectricBill.wav", True, self.location), plus.createSound("Sounds/announcers/Misc_UpTheVoltage.wav", True, self.location), plus.createSound("Sounds/announcers/Misc_JumpStart.wav", True, self.location))
    
    def __del__(self):
        plus.removeSound(self.zapsound)
        plus.removeSound(self.chargesound)
        
        #for x in self.announcer:
            #plus.removeSound(x)
        
        #self.announcer = ()

    def Tick(self):
        #self.announcetimer -= .25
        if self.chargetimer==0.0 and self.NumBotsInRange()==1:
            self.Zap()
            
        if self.zaptimer>0.0:
            self.zaptimer-=.25
            if self.zaptimer<=0.0:
                self.zaptimer = 0.0
                self.zapping = []
                plus.stopSound(self.zapsound)
            elif self.zaptimer>0.0:
                for bot in self.zapping:
                    if not plus.isMatchPaused() and not plus.isMatchOver():
                        plus.damage(bot, 0, 25, plus.getLocation(bot))
                        if self.sensors[bot]:
                            plus.force(bot, 0, 115 * plus.getWeight(bot), 0)
            
        if self.chargetimer > 0.0:
            self.chargetimer -= .25
        elif self.chargetimer<0.0:
            self.chargetimer = 0.0

    def Zap(self):
        if not plus.isMatchPaused() and not plus.isMatchOver():
            if self.chargetimer==0.0:
                for bot, in_range in self.sensors.iteritems():
                    if in_range:
                        plus.zap(bot, 10, 3.0)
                        self.zapping.append(bot)
                        self.zaptimer = 3.0
                        self.chargetimer = 5.0
                        Arenas.currentArena.Charge(self.chargetimer, self.sensors)
                        plus.loopSound(self.zapsound)
                        plus.playSound(self.chargesound)
                        #if self.announcetimer <= 0:
                            #plus.playSound(random.choice(self.announcer))
                            #self.announcetimer = 12.0
        
    def Button(self):
        self.Zap()
        
    def NumBotsInRange(self):
        numBots = 0
        for bot, in_range in self.sensors.iteritems():
            if in_range: numBots += 1
                
        return numBots
        
    def ZoneEvent(self, direction, robot, chassis):
        if chassis:
            r = robot - 1
            if r not in self.sensors: self.sensors[r] = 0
            
            if direction==1:
                self.sensors[r] += 1
            elif direction==-1:
                self.sensors[r] -= 1