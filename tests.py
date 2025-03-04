import unittest
import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from  calculations import calculate_total_daily_calories

class TestCalculateTotalDailyCalories(unittest.TestCase):

    def test_calculate_total_daily_calories(self):
        self.assertEqual(calculate_total_daily_calories(150), 1800)
        self.assertEqual(calculate_total_daily_calories(200), 2400)
        self.assertEqual(calculate_total_daily_calories(100), 1200)
        self.assertEqual(calculate_total_daily_calories(0), 0)
        self.assertEqual(calculate_total_daily_calories(-50), -600)

if __name__ == '__main__':
    unittest.main()