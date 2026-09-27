"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.
    """
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000 :
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.
    """

    efficiency = ((voltage * current)/theoretical_max_power)*100
    if efficiency >= 80 :
        return "green"
    elif efficiency >= 60 :
        return "orange"
    elif efficiency >= 30 :
        return "red"
    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.
    """
    control = temperature * neutrons_produced_per_second
    if control < (0.9*threshold):
        return "LOW"
    elif (0.9*threshold) <= control <= (1.1*threshold):
        return "NORMAL"
    return "DANGER"