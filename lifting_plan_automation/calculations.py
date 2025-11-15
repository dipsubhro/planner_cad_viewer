import math

def calculate_center_of_gravity(load_length, load_width):
    return (load_length / 2, load_width / 2)

def calculate_sling_angle(sling_length, load_width, num_slings):
    if num_slings == 2:
        horizontal_distance = load_width / 2
    elif num_slings == 4:
        horizontal_distance = math.sqrt((load_width/2)**2)
    else:
        horizontal_distance = load_width / 2

    if sling_length > horizontal_distance:
        angle_rad = math.acos(horizontal_distance / sling_length)
        return math.degrees(angle_rad)
    else:
        return 0

def calculate_sling_tension(load_weight, num_slings, sling_angle):
    if sling_angle > 0:
        angle_rad = math.radians(sling_angle)
        tension = (load_weight / num_slings) / math.sin(angle_rad)
        return tension
    else:
        return float('inf')

def check_safety_factors(sling_tension, sling_swl, shackle_swl):
    sling_safety_factor = sling_swl / sling_tension if sling_tension > 0 else 0
    shackle_safety_factor = shackle_swl / sling_tension if sling_tension > 0 else 0
    return (sling_safety_factor, shackle_safety_factor)

def calculate_crane_utilization(load_weight, hook_weight, crane_capacity):
    total_load = load_weight + hook_weight
    utilization = (total_load / crane_capacity) * 100
    return utilization

if __name__ == '__main__':
    load_w = 10000
    load_l = 6
    load_wid = 2.5
    num_s = 4
    sling_l = 5
    sling_s = 5000
    shackle_s = 6000
    hook_w = 500
    crane_cap = 25000

    cog_x, cog_y = calculate_center_of_gravity(load_l, load_wid)
    print(f"Center of Gravity: ({cog_x}, {cog_y})")

    angle = calculate_sling_angle(sling_l, load_wid, num_s)
    print(f"Sling Angle: {angle} degrees")

    tension = calculate_sling_tension(load_w, num_s, angle)
    print(f"Sling Tension: {tension} kg")

    sling_sf, shackle_sf = check_safety_factors(tension, sling_s, shackle_s)
    print(f"Sling Safety Factor: {sling_sf}")
    print(f"Shackle Safety Factor: {shackle_sf}")

    util = calculate_crane_utilization(load_w, hook_w, crane_cap)
    print(f"Crane Utilization: {util}%")
