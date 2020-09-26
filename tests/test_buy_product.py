"""
Test file for buy_product function in vending_machine module
"""
# test_buy_product.property
import pytest
import vending_machine
from vending_machine import InsufficientFunds


def test_drink_275():
    assert vending_machine.buy_product('drink', 275) == 0


def test_chips_225():
    assert vending_machine.buy_product('chips', 225) == 0

def test_candy_315():
    assert vending_machine.buy_product('candy', 315) == 0

def test_banana():
    with pytest.raises(ValueError):
        vending_machine.buy_product('banana', 275)

def test_drink_274():
    with pytest.raises(InsufficientFunds):
        vending_machine.buy_product('drink', 274)
