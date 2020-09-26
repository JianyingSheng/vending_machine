"""
A virtual vending machine
"""

ACC_COIN_LIST=[200,100,25,10,5]# a list of accepted coins value

# a dictionary mapping product and price in cents
PRODUCTS_PRICE={'drink':275,
                'chips':225,
                'candy':315}

# Accepted coins appened to the inserted_coins.
def insert_coin(coin,inserted_coins):
    """
    function
    """
    if  coin not in ACC_COIN_LIST:
        raise ValueError
    inserted_coins.append(coin)

# Check product and balance
def buy_product(product, balance):
    """
    function
    """
    if product not in PRODUCTS_PRICE:
        raise ValueError
    price = PRODUCTS_PRICE[product]
    if balance < price:
        raise InsufficientFunds
    return balance - price

# return changes
def return_change(balance):
    """
    function
    """
    return_coins = []
    balance -= balance % 5
    while balance > 0:
        for coin in ACC_COIN_LIST:
            if balance % coin == 0:
                return_coins.append(coin)
                balance -= coin
                break
    return sorted(return_coins,reverse=True)

class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
