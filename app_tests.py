from nose.tools import *
from bin.app import app
from tests.tools import assert_response

#def test_index():
#    #check that we got a 404 on the / URL
#    resp = app.request('/')
#
    #test our first GET request to /hello
#    resp = app.request("/hello")
#    assert_response(resp)

    #make sure default values work for form
#    resp = app.request("/hello", method="POST")
#    assert_response(resp, contains="Hello")

    #test that we get expected values
#    data = {'name': 'Zed', 'greet': 'Hola'}
#    resp = app.request("/hello", method="POST", data=data)
#    assert_response(resp, contains="Zed")
