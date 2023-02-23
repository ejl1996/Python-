from unittest import TestCase
import caesarcipher

class Test(TestCase):
    def test_caesarcipher_empty_string(self):
        actual_value = caesarcipher.caesarcipher('', False, 5)
        expected_value = ''
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_caesarcipher_alphabetical(self):
        actual_value = caesarcipher.caesarcipher('yzaY-ZABEF', True, 3)
        expected_value = 'bcdB-CDEHI'
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_caesarcipher_numerical(self):
        actual_value = caesarcipher.caesarcipher('14210928', False, 8)
        expected_value = '36432140'
        message = "Test failed"
        self.assertEqual(expected_value, actual_value, message)

    def test_caesarcipher_alphanumerical_true(self):
        actualValue = caesarcipher.caesarcipher('VAxef123Dw', True, 4)
        expectedValue = 'ZEbij567Ha'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_caesarcipher_alphanumerical_false(self):
        actualValue = caesarcipher.caesarcipher('SABSf433Dw', False, 2)
        expectedValue = 'QYZQd211Bu'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)


