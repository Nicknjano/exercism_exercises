def square(number):
    """
    This function calculates the number of grains at each square
    """
    if number < 1 or number > 64 :
        raise ValueError("square must be between 1 and 64")
    grains = 1
    if number == 1 :
        return grains
    i = 1
    while i < number:
        grains = grains * 2
        i+=1
    return grains


def total():
    """
    This function calculates the sum total of grains
    """
    grains = 0
    i=1
    while i <= 64 :
        grains += square(i)
        i+=1
    return grains