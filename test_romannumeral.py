from unittest import TestCase
import romannumeral

class Test(TestCase):
    def test_romannumeral_one(self):
        actualValue = romannumeral.romannumeral(1)
        expectedValue = 'I'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_romannumeral_fifty(self):
        actualValue = romannumeral.romannumeral(53)
        expectedValue = 'LIII'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_romannumeral_one_hundred(self):
        actualValue = romannumeral.romannumeral(132)
        expectedValue = 'CXXXII'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_romannumeral_five_hundred(self):
        actualValue = romannumeral.romannumeral(523)
        expectedValue = 'DXXIII'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_romannumeral_more_than_thousand(self):
        actualValue = romannumeral.romannumeral(1032)
        expectedValue = 'MXXXII'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

