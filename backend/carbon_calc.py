def calculate_travel_footprint(distance_km, mode):
    factors = {"car": 0.21, "bus": 0.05, "flight": 0.15}

    # Handle negative distance
    if distance_km < 0:
        return 0.0

    # Normalize mode (case-insensitive)
    mode = mode.lower()

    return distance_km * factors.get(mode, 0.0)

