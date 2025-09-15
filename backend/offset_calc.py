def calculate_offsets(distance, mode):
    factors = {
        "Car": 0.21,
        "Bus": 0.11,
        "Train": 0.06,
        "Flight": 0.30,
        "Bike": 0.0
    }
    emissions = distance * factors.get(mode, 0.2)
    trees_needed = int(emissions / 21.77) + 1
    return emissions, trees_needed
