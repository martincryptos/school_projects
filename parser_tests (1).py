from ex48.parser import *
from nose.tools import *

def test_peek():
    assert_raises(TypeError, parse_sentence, 3, 4, 5)

def test_sentence_parser():
    x = parse_sentence([('noun', 'bear'), ('verb', 'run'), ('direction', 'south')])
    assert_equal(x.subject, 'bear')
    assert_equal(x.object, 'south')
    assert_equal(x.verb, 'run')

def test_peek():
    x = peek([('hello', 'test')])
    assert_equal(x, 'hello')

#  def test_match():

def test_parse_subject():
    assert_raises(ParserError, parse_subject, 'hola')

def test_parse_object():
    assert_raises(TypeError, parse_object, 234)
