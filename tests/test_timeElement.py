import unittest
from datetime import datetime, timedelta
from wtt import timeElement, timeType



class TestTimeElement(unittest.TestCase):

    def test_return_workingHours(self):
        a = timeElement(timeType.vecation,datetime(2020,4,27),timedelta(hours=1))
        self.assertEqual(a.workingHours,timedelta(hours=1))
        a.workingHours = timedelta(hours=2)
        self.assertEqual(a.workingHours, timedelta(hours=2))
        a.workingHours = timedelta(hours=-5)
        self.assertEqual(a.workingHours, timedelta(hours=-5))

    def test_add_workingHours(self):
        a = timeElement(timeType.flexitime,datetime(2020,4,27),timedelta(hours=-1))
        b = timeElement(timeType.vecation,datetime(2020,4,27),timedelta(hours=5))
        self.assertEqual(a+b, timedelta(hours=4))
        a = timeElement(timeType.flexitime,datetime(2020,4,27),timedelta(hours=-6))
        self.assertEqual(a+b, timedelta(hours=-1))
        with self.assertRaises(ValueError):
            a = timeElement(timeType.flexitime,datetime(2020,4,27),timedelta(hours=1))


if __name__ == "__main__":
    unittest.main()