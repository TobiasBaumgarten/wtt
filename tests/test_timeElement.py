import unittest
from datetime import datetime, timedelta
from wtt import timeElement, timeType



class TestTimeElement(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1+1,2)

    def test_return_workingHours(self):
        a = timeElement(timeType.vecation,datetime(2020,4,27),timedelta(hours=1))
        self.assertEqual(a.workingHours,timedelta(hours=2))

if __name__ == "__main__":
    unittest.main()