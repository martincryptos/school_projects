import web
from paste.fixture import TestApp
from nose.tools import *
from gothonweb.map import *
from bin.app import *
from tests.tools import assert_response

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab.  There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_modify_paths():
    opening = Room("Noises", "You hear noises.")
    choice_2_up = Room("Dragons", "There are dragons here, you must fight.")
    choice_2_down = Room("Goblins", "There are goblins here, you can run.")
    die = Room("dead", "you are dead.")

    opening.add_paths({'dragon': choice_2_up, 'goblin': choice_2_down})
    choice_2_up.add_paths({'death': opening})
    choice_2_down.add_paths({'too_slow': opening})

    assert_equal(opening.go('dragon'), choice_2_up)
    assert_equal(opening.go('goblin'), choice_2_down)
    assert_equal(opening.go('dragon').go('death'), opening)
    assert_equal(opening.go('goblin').go('too_slow'), opening)

def test_central_corridor():
    assert_equal(START.go('shoot!'), generic_death)
    assert_equal(START.go('dodge!'), generic_death_a)

    room = START.go("tell a joke")
    assert_equal(room, laser_weapon_armory)

def test_escape_pod():
    assert_equal(escape_pod.paths[('2')], the_end_winner)
    assert_equal(escape_pod.paths[('*')], the_end_loser)

def test_the_bridge():
    assert_equal(the_bridge.paths[('throw the bomb')], generic_death_b)
    assert_equal(the_bridge.paths[('slowly place the bomb')], escape_pod)

def test_laser_weapon_armory():
    assert_equal(laser_weapon_armory.paths[('0132')], the_bridge)
    assert_equal(laser_weapon_armory.paths[('*')], generic_death_c)

def test_app():
    middleware = []
    testApp = TestApp(app.wsgifunc(*middleware))
    r = testApp.get('/')
    assert_equal(r.status, 303)

def test_app_ext():
    x = GameEngine()
    y = x.GET()
    assert_equal(y, render.you_died())
