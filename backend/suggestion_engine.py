def get_suggestions(footprint: float):
    """
    Suggest eco-friendly actions based on footprint value.
    """
    if footprint > 1000:
        return [
            "Switch to renewable energy sources ⚡",
            "Consider using public transport 🚌",
            "Plant more trees 🌳",
            "Reduce long-distance flights ✈️"
        ]
    elif footprint > 500:
        return [
            "Carpool with colleagues 🚗",
            "Use water-saving appliances 💧",
            "Work remotely a few days a week 💻"
        ]
    else:
        return [
            "Great job! Keep up your eco-friendly practices 🌱",
            "Encourage others to follow your steps 👥"
        ]

