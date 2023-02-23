from unittest import TestCase
import phone

class Test(TestCase):

    def test_phone_empty_string(self):
        actualValue = phone.phone("")
        expectedValue = ''
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_phone_alphabetical(self):
        actualValue = phone.phone("ABC-CDE-FASG")
        expectedValue = '222-233-3274'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_phone_numerical(self):
        actualValue = phone.phone("604-123-2348")
        expectedValue = '604-123-2348'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)

    def test_phone_alphanumerical(self):
        actualValue = phone.phone("604-APZ-2348")
        expectedValue = '604-279-2348'
        message = "Test failed"
        self.assertEqual(expectedValue, actualValue, message)