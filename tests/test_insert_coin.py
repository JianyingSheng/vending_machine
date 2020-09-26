"""
Test file for insert_coin in vending_machine
"""
#test_insert_coin.py
import  pytest
import  vending_machine


def test_five_cents():
    inserted_coins = []
    vending_machine.insert_coin(5,inserted_coins)
    assert inserted_coins == [5]

def test_ten_cents():
    inserted_coins = []
    vending_machine.insert_coin(10,inserted_coins)
    assert inserted_coins == [10]

def test_twentyfive_cents():
    inserted_coins = []
    vending_machine.insert_coin(25,inserted_coins)
    assert inserted_coins == [25]

def test_onehundred_cents():
    inserted_coins = []
    vending_machine.insert_coin(100,inserted_coins)
    assert inserted_coins == [100]

def test_twohundred_cents():
    inserted_coins = []
    vending_machine.insert_coin(200,inserted_coins)
    assert inserted_coins == [200]

def test_fifty_cents():
    inserted_coins = []
    with pytest.raises(ValueError):
        vending_machine.insert_coin(50,inserted_coins)
