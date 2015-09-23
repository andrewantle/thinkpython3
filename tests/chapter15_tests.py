from nose.tools import *
from thinkpython3.chapter15 import *


def setup():
    print("SETUP!")



def teardown():
    print("TEARDOWN!")



def test_card():
    card = Card(1, 11)
    print(card)
    assert str(card) == 'Jack of Diamonds'
