"Initialize the Arenas module"

from __future__ import generators
import plus
import math
import string
import random

arenas = []
currentArena = None

class Camera(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def apply(self):
        plus.setCameraPosition(self.position[0], self.position[1], self.position[2])

class StaticCamera(Camera):
    def __init__(self, name, position, rotation, fov):
        Camera.__init__(self, name, position)
        self.rotation = rotation
        self.fov = fov

    def apply(self):
        Camera.apply(self)
        plus.setCameraRotation(self.rotation[0], self.rotation[1])
        plus.setCameraFOV(self.fov)

class WatchCamera(Camera):
    def __init__(self, name, position, range):
        Camera.__init__(self, name, position)
        self.range = range

    def apply(self):
        Camera.apply(self)
        plus.setCameraFOVRange(self.range[0], self.range[1], self.range[2], self.range[3])

class SuperArena(plus.Arena):
    "Python base class of the C++ Arena."
    name = "No Name"
    preview = "No Preview"
    in_list = True
    game_types = []
    extent = (-15.0, 15.0, 15.0, -15.0)

    def __init__(self, modelfile):
        plus.Arena.__init__(self, modelfile)

        self.StaticCams = []
        self.StaticCamIterator = iter(self.StaticCams)
        self.WatchCams = []
        self.WatchCamIterator = iter(self.WatchCams)

        self.bHazardsOn = False
        self.hazards = []

        self.Intro = None
        self.bDoingIntro = False
        self.introPause = 0
        self.intro_sounds = {}                 # list of sounds used by intro
        self.intro_music = None
        self.endmusic = None

        mapfile = string.replace(modelfile, "gmf", "map")
        self.LoadMap(mapfile)

    def __del__(self):
        if self.endmusic:
            plus.stopSound(self.endmusic)
            plus.removeSound(self.endmusic)
        
    def Activate(self, on):
        if on:
            # get rid of intro generator to avoid leaks
            self.Intro = None

    def Winner(self, id1, id2):
        #print "Winners:", id1, id2
        self.endmusic = plus.createSound("Sounds/intro_music/hopp_club.wav", False, (0,0,0))
        plus.setVolume(self.endmusic, 0, 0)
        plus.loopSound(self.endmusic)
        commentOpt = ("End_MatchIsOver.wav", "End_MatchIsDone.wav", "End_GreatMatch.wav")
        annc = plus.createSound("Sounds/announcers/"+random.choice(commentOpt), False, (0,0,0))
        plus.playOnce(annc)

    def AddShadowReceivers(self):
        "Add surfaces for shadows to fall on."
        pass

    def Tick(self):
        if self.bDoingIntro:
            self.introPause -= self.tickInterval
            if self.introPause <= 0:
                self.introPause = self.Intro.next()
                if self.introPause == 0:
                    self.DoIntro(False)

        return plus.Arena.Tick(self)

    def DoIntro(self, on):
        if on:
            self.Intro = self.Introduction()
            self.bDoingIntro = True
        else:
            self.bDoingIntro = False
            # start cams over from first camera
            self.StaticCamIterator = iter(self.StaticCams)
            self.WatchCamIterator = iter(self.WatchCams)

            for sound in self.intro_sounds.itervalues():
                plus.stopSound(sound)
                plus.removeSound(sound)

            if self.intro_music:
                plus.stopSound(self.intro_music)
                plus.removeSound(self.intro_music)

            plus.introComplete()

    def Introduction(self):
        "Default introduction waits one second, then goes."
        yield 1
        yield 0

    def HazardsOn(self, on):
        self.bHazardsOn = on
        self.SetMapHazardsOn(on)
        return True

    def AddHazard(self, hazard):
        "Register a hazard so the AI can find them."
        self.hazards.append(hazard)

    def GetNearestHazard(self, location):
        "Return the hazard nearest to this location or None."
        if self.bHazardsOn and len(self.hazards) > 0:
            closest = None
            min_distance = 999
            for each in self.hazards:
                distance = math.hypot(each.location[0] - location[0], each.location[2] - location[2])
                if distance < min_distance:
                    min_distance = distance
                    closest = each
            return closest
        else:
            return None

    def AddStaticCamera(self, name, position, rotation, fov):
        self.StaticCams.append(StaticCamera(name, position, rotation, fov))

    def AddWatchCamera(self, name, position, range):
        self.WatchCams.append(WatchCamera(name, position, range))
        
    def NextStaticCamera(self):
        if len(self.StaticCams) > 0:
            try:
                camera = self.StaticCamIterator.next()
            except StopIteration:
                self.StaticCamIterator = iter(self.StaticCams)
                camera = self.StaticCamIterator.next()

            camera.apply()

            return camera.name
        else:
            return ""

    def NextWatchCamera(self):
        if len(self.WatchCams) > 0:
            try:
                camera = self.WatchCamIterator.next()
            except StopIteration:
                self.WatchCamIterator = iter(self.WatchCams)
                camera = self.WatchCamIterator.next()

            camera.apply()
            
            return camera.name
        else:
            return ""

    def NextAutoCamera(self):
        return ""

    def CreateMap(self, resolution, down = 6.0):
        "Map out this arena into memory."

        # given a starting grid size and resolution,
        # map out the floor height (top-down)
        # then, map the walls (left-right, forward-back)
        diag = math.sqrt(pow(resolution, 2) + pow(resolution, 2)) / 2.0

        y0 = self.GetStartPointLocation(0)[1] + 2   # height (y) of start point 0
        y1 = y0 - down                               # down x meters (default is 6)

        cols = int((self.extent[2] - self.extent[0]) / resolution)
        rows = int((self.extent[1] - self.extent[3]) / resolution)

        Floor = [ [None] * rows for i in range(cols)]
        Walls = [ [0] * rows for i in range(cols)]
        Height = [None, None]

        z = self.extent[1]
        for j in range(rows):
            x = self.extent[0]
            for i in range(cols):
                # first check for floor
                result = self.RayTest((x, y0, z), (x, y1, z))
                if result[0]:
                    hit = result[1]
                    Floor[i][j] = hit[1]

                    if Height[0] is None or Floor[i][j] > Height[0]: Height[0] = Floor[i][j]
                    if Height[1] is None or Floor[i][j] < Height[1]: Height[1] = Floor[i][j]

                # now check for walls (once we've found at least one floor)
                if Height[0] != None:
                    yy0, yy1 = 0, 0
                    if result[0]:
                        yy0 = Floor[i][j] + 1.0
                        yy1 = Floor[i][j] + .5
                    else:
                        yy0 = Height[0] + 1.0
                        yy1 = Height[0] + .5
                
                    p1 = (x - resolution * diag, yy0, z - resolution * diag)
                    p2 = (x + resolution * diag, yy1, z + resolution * diag)
                    result = self.RayTest(p1, p2)
                    if result[0]:
                        Walls[i][j] = 1
                    else:
                        p1 = (x - resolution * diag, yy0, z + resolution * diag)
                        p2 = (x + resolution * diag, yy1, z - resolution * diag)
                        result = self.RayTest(p1, p2)
                        if result[0]:
                            Walls[i][j] = 1

                x += resolution
            z -= resolution

        if Height[0]:
            self.SetMapSize(cols, rows)
            self.SetMapResolution(resolution)
            self.SetMapAltitude(Height[0])

            for j in range(rows):
                for i in range(cols):
                    if Walls[i][j] == 1: self.SetMapWall(i, j)
                    elif Floor[i][j] != None:
                        diff = int(round(Floor[i][j] - Height[0], 1) / .1)
                        self.SetMapHeight(i, j, diff)
        else:
            print "cols, rows:", cols, rows
            print "altitude:", Height[0]
                
    def SaveMap(self, filename):
        "Save map from memory to file."
        try:
            output = file(filename, "w")

            cols = int((self.extent[2] - self.extent[0]) / self.GetMapResolution())
            rows = int((self.extent[1] - self.extent[3]) / self.GetMapResolution())

            output.write(self.name + "\n")
            output.write(str(self.extent) + "\n")
            output.write(str(self.GetMapResolution()) + "\n")
            output.write(str(self.GetMapAltitude()) + "\n")

            for j in range(rows):
                for i in range(cols):
                    if self.IsMapWall(i, j):
                        output.write("XX ")
                    elif self.IsMapHazard(i, j):
                        output.write("!! ")
                    elif self.IsMapEmpty(i, j):
                        output.write(".. ")
                    else:
                        output.write(string.rjust(str(-self.GetMapHeight(i, j)), 2) + " ")
                output.write("\n")
        except IOError:
            print "Couldn't write map file."

    def LoadMap(self, filename):
        try:
            input = file(filename, "r")

            input.readline() # skip name
            self.extent = eval(input.readline())
            resolution = eval(input.readline())
            max_height = eval(input.readline())

            cols = int((self.extent[2] - self.extent[0]) / resolution)
            rows = int((self.extent[1] - self.extent[3]) / resolution)

            self.SetMapSize(cols, rows)
            self.SetMapExtent(self.extent)
            self.SetMapResolution(resolution)
            self.SetMapAltitude(max_height)

            for j in range(rows):
                i = 0
                elements = string.split(input.readline())
                for each in elements:
                    if each == 'XX':
                        self.SetMapWall(i, j)
                    elif each == '!!':
                        self.SetMapHazard(i, j)
                    elif each != '..':
                        self.SetMapHeight(i, j, -int(each))
                    i += 1
        except IOError:
            print "No map file found."

def sortByName(x, y):
    if x.name < y.name:
        return -1
    elif x.name > y.name:
        return 1
    else:
        return 0

def register(arena):
    "Called by derived Arenas to keep a master list of available arena types."
    if issubclass(arena, SuperArena):
        extant = [x for x in arenas if x.name == arena.name]
        if len(extant) == 0:
            arenas.append(arena)

            print "We now have", len(arenas), "arenas!"

def enumAvailable(type):
    "Return a list of available arenas via the C++ enumArena function."
    list = [x for x in arenas if x.in_list and type in x.game_types]
    list.sort(sortByName)
    for each in list:
        a = plus.ArenaDetail()
        a.name = each.name
        a.preview = each.preview
        a.description = each.__doc__
        a.id = id(each)

        plus.enumArena(a)

def createArena(idnumber):
    "Call C++ setArena for the arena entry with this id."
    list = [x for x in arenas if id(x) == idnumber]
    if len(list) > 0:
        print "Creating arena", list[0].name
        global currentArena
        newArena = list[0]()
        plus.setArena(newArena)
        currentArena = newArena

def createArenaByName(name):
    "Call C++ setArena for the arena entry with this name."
    list = [x for x in arenas if x.name == name]
    if len(list) > 0:
        print "Creating arena", list[0].name
        global currentArena
        newArena = list[0]()
        plus.setArena(newArena)
        currentArena = newArena

def clearArena():
    global currentArena
    currentArena = None

import Practice