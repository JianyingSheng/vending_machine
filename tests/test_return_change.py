"""
Test file for return_change function in vending_machine
"""
#test_return_change.py
import vending_machine

def test_0_balance():
    assert vending_machine.return_change(0) == []


def test_25_balance():
    assert vending_machine.return_change(25) == [25]

def test_400_balance():
    assert vending_machine.return_change(400) == [200,200]

def test_300_balance():
    assert vending_machine.return_change(300) == [200,100]

def test_265_balance():
    assert vending_machine.return_change(265) == [200, 25, 25, 10, 5]

def test_7_balance():
    assert vending_machine.return_change(7) == [5]

def test_negative_balance():
    assert vending_machine.return_change(-5) == []
