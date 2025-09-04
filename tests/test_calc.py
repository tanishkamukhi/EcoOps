import unittest
from backend.carbon_calc import calculate_travel_footprint

class TestCarbonCalc(unittest.TestCase):

    def test_car_footprint(self):
        self.assertAlmostEqual(calculate_travel_footprint(100, "car"), 21.0)

    def test_bus_footprint(self):
        self.assertAlmostEqual(calculate_travel_footprint(100, "bus"), 5.0)

    def test_flight_footprint(self):
        self.assertAlmostEqual(calculate_travel_footprint(100, "flight"), 15.0)

    def test_invalid_mode_returns_zero(self):
        self.assertEqual(calculate_travel_footprint(50, "train"), 0.0)

    def test_zero_distance(self):
        self.assertEqual(calculate_travel_footprint(0, "car"), 0.0)

    def test_negative_distance(self):
        # Negative distance should ideally return 0, or you can decide to raise ValueError
        self.assertEqual(calculate_travel_footprint(-100, "car"), 0.0)

    def test_case_insensitivity(self):
        # If your function doesn’t handle this yet, you can add .lower() in implementation
        self.assertAlmostEqual(calculate_travel_footprint(100, "CAR"), 21.0)

    def test_large_distance(self):
        # Stress test with large number
        self.assertAlmostEqual(calculate_travel_footprint(1000000, "bus"), 50000.0)

if __name__ == "__main__":
    unittest.main()
