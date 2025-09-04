import unittest
from backend.suggestion_engine import get_suggestions

class TestSuggestionEngine(unittest.TestCase):

    def test_high_footprint(self):
        suggestions = get_suggestions(2000)
        self.assertIn("Switch to renewable energy", suggestions)

    def test_low_footprint(self):
        suggestions = get_suggestions(200)
        self.assertIn("Keep up eco-friendly practices", suggestions)

    def test_boundary_value(self):
        # Exactly 1000 (check threshold)
        suggestions = get_suggestions(1000)
        self.assertTrue(isinstance(suggestions, list))

if __name__ == "__main__":
    unittest.main()
