"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    """
    if power_pellet_active == True and touching_ghost == True :
        return True
    return False


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.
    """
    if touching_power_pellet == True or touching_dot == True :
        return True
    return False


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.
    """
    if power_pellet_active == False and touching_ghost == True :
        return True
    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.
    """

    if has_eaten_all_dots == True and lose(power_pellet_active, touching_ghost) == False :
        return True
    return False
