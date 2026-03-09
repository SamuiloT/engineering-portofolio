import math

def simulate_projectile(v0, angle_deg):
    g = 9.81
    angle_rad = math.radians(angle_deg)

    t_flight = (2 * v0 * math.sin(angle_rad)) / g
    max_height = (v0**2 * math.sin(angle_rad)**2) / (2 * g)
    range_m = (v0**2 * math.sin(2 * angle_rad)) / g

    print(f"Launch velocity: {v0} m/s at {angle_deg} degrees")
    print(f"Time of flight:  {t_flight:.2f} seconds")
    print(f"Max height:      {max_height:.2f} meters")
    print(f"Range:           {range_m:.2f} meters")


simulate_projectile(1500, 20)

