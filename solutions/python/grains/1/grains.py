def square(number):
    if number < 1 or number > 64 :
        raise ValueError("square must be between 1 and 64")
    grains = 1
    if number == 1 :
        return grains
    for i in range(1, number):
        grains = grains * 2
    return grains


def total():
    grains = 0
    for i in range(1, 65) :
        grains += square(i)
    return grains