'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

def divisionByTwo(number):
    return number / 2

divisionByTwo(0)
import unittest
class MyTestCase(unittest.TestCase):

    def test_divisionByTwo(self):
        self.assertEqual(divisionByTwo(4),2)
        self.assertIsNot(divisionByTwo(10),10)

        self.assertGreater(divisionByTwo(10),10)


