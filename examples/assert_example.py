market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # an assert statement is a sanity check
    # assertions are for detecting programmer errors
    # raise and exceptions are for handling user errors
    # if assert statement fails, the program should crash
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)



print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
