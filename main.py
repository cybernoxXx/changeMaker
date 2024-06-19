def makeChange(amount):
    dict_to_coins = {}

    # In all cases the if checks if the change can be composed of the relative coin. If yes it added the correct amount of che corrispective coin to the dictionary and subtract the total to the amount
    if amount % 25 != amount:
        dict_to_coins['quarters'] = amount // 25
        amount -= 25*(amount//25)
    if amount % 10 != amount:
        dict_to_coins['dimes'] = amount // 10
        amount -= 10*(amount//10)
    if amount % 5 != amount:
        dict_to_coins['nickels'] = amount // 5
        amount -= 5*(amount//5)
    if amount % 1 != amount:
        dict_to_coins['pennies'] = amount // 1
        amount -= 1*(amount//1)

    return dict_to_coins


assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
