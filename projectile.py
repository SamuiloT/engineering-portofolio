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


simulate_projectile(100, 45)
simulate_projectile(100, 30)
simulate_projectile(100, 60)

def find_max_range(v0):
    max_range = 0
    best_angle = 0
    for angle in range(1, 90):
        angle_rad = math.radians(angle)
        range_m = (v0**2 * math.sin(2 * angle_rad)) / 9.81
        if range_m > max_range:
            max_range = range_m
            best_angle = angle
    print(f"For v0={v0} m/s: best angle = {best_angle} degrees, max range = {max_range:.2f} meters")

find_max_range(100)
find_max_range(500)
find_max_range(1000)