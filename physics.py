from ursina import time

def apply_physics(aircraft, throttle=50):
    # Basic aerodynamic simulation
    rho = 1.225  # Air density
    v = aircraft.speed
    S = 3        # Wing area
    Cl = 1.2     # Lift coefficient

    Lift = 0.5 * rho * (v ** 2) * S * Cl
    aircraft.y += (Lift / 10000) * time.dt