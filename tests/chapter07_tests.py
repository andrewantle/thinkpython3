from nose.tools import *
from thinkpython3.chapter07 import find_first_index


def setup():
    print("SETUP!")


def teardown():
    print("TEARDOWN!")


def test_find_first_index():
    source_string = "I Love Star Trek"
    
    index = find_first_index(source_string, 'o')
    assert index == 3

    index = find_first_index(source_string, 'z')
    assert index == -1
    
    index = find_first_index("", 'x')
    assert index == -1
    
    index = find_first_index(source_string, 'e', 6)
    assert index == 14
    
    index = find_first_index(source_string, 'o', "Hola")
    assert index == 3
