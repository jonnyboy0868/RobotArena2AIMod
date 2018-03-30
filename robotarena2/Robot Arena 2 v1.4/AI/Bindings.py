import math

def load(list):
    print "Loading AI bindings"

    # binding format:
    # ( 'name of robot from .bot file', 'name of AI from script class',
    #       {'optional constructor parameter':value, 'another':value} )

    # constructor parameters:
    # nose - "front" of bot in radians (default 0)
    # invertible - can function upside-down (default False)
    # topspeed - speed in meters/second AI will attempt not to exceed (default 4.0)
    # throttle - maximum analog value AI will attempt not to exceed (default 100)
    # turnspeed - turning in radians/second AI will attempt not to exceed (default 2.5)
    # turn - maximum analog value AI will attempt not to exceed (default 60)
    # radius - bot radius to use for checking for hazards and walls (default 1.0)
    
    list.append( ("ALARM", "Poker", { 'topspeed': 12.0, 'throttle': 110, 'turn':80, 'turnspeed':1.5, 'weapons': (13,) }) )
    list.append( ("Arc Pounder", "Whipper", { 'invertible': True, 'whip': "around", 'zone': "swing", 'turnspeed':1.5, 'turn':80, 'topspeed':12.0, 'throttle': 110, 'weapons':(14,) }) )
    list.append( ("BackSlash", "Flipper", { 'nose' : math.pi, 'topspeed' : 9, 'throttle' : 115, 'turn':80, 'weapons': (16, 17) }) )
    list.append( ("Backyard Ripper", "DirectionalSpinner", { 'nose': math.pi, 'topspeed' : 12.0, 'throttle' : 115, 'turnspeed': 2.0, 'weapons': (16, 17, 18, 19) }) )
    list.append( ("BEAR", "Chopper", { 'radius':1.4, 'triggers': ['LeftPaw', 'RightPaw'], 'topspeed' : 9.0, 'throttle': 110, 'turnspeed': 1.0, 'weapons': (13, 14) }) )
    list.append( ("Berserker", "Spinner", { 'topspeed' : 10.0, 'throttle' : 110.0, 'weapons': (8, 9, 10) }) )
    list.append( ("Big Dog", "Pusher", { 'radius': 1.4, 'nose' : math.pi , 'topspeed':4.0, 'turnspeed' : 3.5 }) )
    list.append( ("BOT-204", "DirectionalSpinner", { 'radius':1.2, 'trigger' : 'spin', 'turnspeed' : 1.15, 'topspeed' : 12, 'throttle' : 120, 'weapons': (6,) }) )
    list.append( ("Bushido", "Chopper", { 'topspeed' : 12.0 , 'turnspeed' : 1.5 , 'throttle' : 120, 'weapons': (15,) }) )
    list.append( ("CatFish", "Rammer", { 'topspeed' : 8.0, 'turnspeed' : 1.75 }) )
    list.append( ("Civil Disobedience", "Rammer", { 'turnspeed' : 1.75 }) )
    list.append( ("Coal Miner", "DirectionalSpinner", { 'invertible': True, 'nose': math.pi, 'trigger' : 'twirl', 'topspeed': 12.0, 'turnspeed': 2.0, 'throttle': 110, 'weapons': (21, 22) }) )
    list.append( ("Da Dog", "Pusher", { 'nose' : math.pi , 'turnspeed' : 2.0 }) )
    list.append( ("DEADBEAT", "Chopper", { 'topspeed' : 10.0, 'weapons': (7,) }) )
    list.append( ("Dementia", "Flipper", { 'turnspeed' : 0.8, 'topspeed' : 12, 'weapons': (13,) }) )
    list.append( ("Devil", "Pusher", { 'radius' : 1.3, 'turn' : 5 }) )
    #list.append( ("EMERGENCY", "Flipper", { 'radius':1.2, 'nose': math.pi, 'car': True, 'topspeed': 12.0, 'turn': 20, 'weapons': (11,) }) )
    list.append( ("EMERGENCY", "Flipper", { 'radius':1.5, 'topspeed': 12.0, 'turn': 20, 'weapons': (29, 30) }) )
    list.append( ("Eye Poker", "Rammer", { 'invertible': True, 'turnspeed' : 1.5, 'topspeed' : 12.0 }) )
    list.append( ("Flame Chopper", "Chopper", { 'radius':1.1, 'topspeed' : 12.0 , 'turnspeed' : 2.0 , 'throttle' : 120, 'weapons': (8,) }) )
    list.append( ("FlapJack", "Flipper", { 'topspeed' : 12, 'throttle' : 120, 'weapons': (10,) }) )
    list.append( ("Grog, The Warrior", "Chopper", { 'radius':1.4, 'topspeed' : 12.0, 'turnspeed': 1.0, 'weapons': (8,) }) )
    list.append( ("Hanky Panky", "Flipper", { 'topspeed' : 12.0, 'weapons': (15,) }) )
    list.append( ("Iceberg", "Chopper", { 'radius':1.2, 'nose' : math.pi , 'topspeed' : 12 , 'throttle' : 110, 'turnspeed': 1.0, 'weapons': (13, 16) }) )
    list.append( ("JACKPOT!", "Chopper", { 'topspeed' : 12.0 , 'turnspeed' : 1.25 , 'throttle' : 130, 'weapons': (11,) }) )
    list.append( ("Lil' Dog", "Rammer", { 'nose': math.pi, 'turnspeed': 1.5 }) )
    list.append( ("Little Metal Friend", "LittleMetalFriend", {}) )
    #list.append( ("Little Metal Friend", "Whipper", { 'invertible': True, 'zone': "squeeze", 'turnspeed' : 1.0, 'topspeed' : 12.0, 'weapons': (8, 12) }) )
    list.append( ("LugNut", "Rammer", { 'radius':1.2, 'nose' : -math.pi / 2, 'turnspeed' : 1.0, 'topspeed' : 12.0, 'throttle' : 120 }) )
    list.append( ("M.A.D.", "Rammer", { 'topspeed' : 12.0, 'throttle' : 120 }) )
    list.append( ("MiniBerg", "Chopper", { 'nose' : math.pi , 'topspeed' : 12.0 , 'turnspeed' : 1.75 , 'throttle' : 120, 'weapons': (12,) }) )
    list.append( ("Mud Runner", "Chopper", { 'radius': 1.4, 'topspeed' : 7.0, 'throttle' : 110, 'weapons' : (10, 12) }) )
    list.append( ("Ninja", "DirectionalSpinner", { 'turnspeed' : 1.0, 'topspeed' : 12.0, 'throttle' : 120, 'weapons': (7, 8) }) )
    list.append( ("Raptor", "Chopper", { 'radius': 1.3, 'nose' : math.pi , 'topspeed' : 12 , 'throttle' : 110 , 'turnspeed' : 1.25, 'weapons': (14, 15) }) )
    list.append( ("Razor", "Rammer", { 'nose': math.pi, 'turnspeed' : 1.25 }) )
    list.append( ("REVENGE", "DirectionalSpinner", { 'turnspeed' : 1.25, 'topspeed' : 12.0, 'throttle' : 110, 'weapons': (4,) }) )
    list.append( ("Ripblade", "DirectionalSpinner", { 'nose': math.pi, 'topspeed' : 12.0, 'throttle' : 110, 'turnspeed': 1.5, 'weapons': (25, 26) }) )
    list.append( ("Roly Poly", "Rammer", { 'nose': math.pi, 'turnspeed' : 1.0 }) )
    list.append( ("Ronin", "Rammer", { 'radius': 1.5, 'invertible': True, 'turnspeed' : 1.0 }) )
    list.append( ("SaberTooth", "Whipper", { 'topspeed' : 12.0, 'throttle' : 110, 'turnspeed' : 1.5, 'weapons': (9, 10) }) )
    list.append( ("Scout", "Flipper", { 'topspeed' : 12.0, 'throttle' : 140, 'turnspeed': 2.0, 'weapons': (9,) }) )
    list.append( ("Sentinel", "Flipper", { 'radius':1.4, 'car': True, 'topspeed' : 12.0, 'throttle' : 110, 'weapons': (11,) }) )
    list.append( ("SnowJob", "Pusher", { 'radius':1.5, 'turnspeed' : 1.5 }) )
    list.append( ("Stinger", "Poker", { 'radius':1.1, 'nose' : math.pi, 'turnspeed' : 1.0, 'turn' : 20.0, 'topspeed' : 12.0, 'throttle' : 120, 'weapons': (9,) }) )
    list.append( ("The Boxer", "Poker", { 'triggers' : ["JabLeft", "JabRight"], 'topspeed' : 12.0, 'throttle' : 125, 'turnspeed' : 1.5, 'weapons': (15, 16) }) )
    list.append( ("Tornado", "Spinner", { 'radius':1.2, 'nose' : -math.pi / 2, 'range' : 4.0, 'topspeed' : 12.0, 'throttle': 120, 'turnspeed' : 1.75, 'weapons': (16, 17, 19, 23) }) )
    list.append( ("Wide Load", "Poker", { 'radius':1.2, 'nose' : math.pi, 'turnspeed' : 1.0, 'topspeed' : 12.0, 'throttle' : 110, 'weapons': (18, 19, 20, 21) }) )
    list.append( ("Insanity_2", "DirectionalSpinner", { 'nose': math.pi, 'topspeed' : 12.0, 'throttle' : 110, 'turnspeed': 4.0, 'weapons': (17,16) }) )
    list.append( ("BotX", "DirectionalSpinner", {'nose': math.pi, 'topspeed': 4.0, 'throttle':100, 'turnspeed':2.5, 'weapons':(1,3) }) )
    list.append( ("Sledge", "Chopper", { 'radius': 1.3, 'nose' : math.pi , 'topspeed' : 12 , 'throttle' : 110 , 'turnspeed' : 1.25, 'weapons': (74,) }) )
	
