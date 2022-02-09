from nose.tools import *
from ex48 import lexicon_v_2

def test_directions():
    assert_equal(lexicon_v_2.scan("north"), [('direction', 'north')])
    result = lexicon_v_2.scan("north south east west up down left right back hoopla hippling")
    assert_equal(result, [('direction', 'north'),
                                ('direction', 'south'),
                                ('direction', 'east'),
                                ('direction', 'west'),
                                ('direction', 'up'),
                                ('direction', 'down'),
                                ('direction', "left"),
                                ('direction', 'right'),
                                ('direction', 'back'),
                                ('direction', 'hoopla'),
                                ('direction', 'hippling')])

def test_verbs():
    assert_equal(lexicon_v_2.scan('go'), [('verb', 'go')])
    result = lexicon_v_2.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat')])
def test_stops():
    assert_equal(lexicon_v_2.scan('the'), [('stop', 'the')])
    result = lexicon_v_2.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                            ('stop', 'in'),
                            ('stop', 'of')])
def test_nouns():
    assert_equal(lexicon_v_2.scan("bear"), [('noun', 'bear')])
    result = lexicon_v_2.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                            ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon_v_2.scan("1234"), [('number', 1234)])
    result = lexicon_v_2.scan("3 91234")
    assert_equal(result, [('number', 3),
                            ('number', 91234)])

def test_errors():
    assert_equal(lexicon_v_2.scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result = lexicon_v_2.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                            ('error', 'ias'),
                            ('noun', 'princess')])
