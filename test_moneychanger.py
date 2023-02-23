from unittest import TestCase
import moneychanger


class Test(TestCase):
    def test_moneychanger_zero(self):
        actualValue = moneychanger.moneychanger(0)
        expectedValue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_moneychanger_coins(self):
        actualValue = moneychanger.moneychanger(1.53)
        expectedValue = [0, 0, 0, 0, 0, 0, 1, 3, 0, 0]
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_moneychanger_bills(self):
        actualValue = moneychanger.moneychanger(70.00)
        expectedValue = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_moneychanger_bills_and_coins(self):
        actualValue = moneychanger.moneychanger(66.54)
        expectedValue = [0, 1, 0, 1, 1, 0, 1, 2, 0, 1]
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_moneychanger_more_than_hundred(self):
        actualValue = moneychanger.moneychanger(140.22)
        expectedValue = [1, 0, 2, 0, 0, 0, 0, 0, 2, 0]
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

