'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''

def MakeLowercase(name):
    return name.lower()


import unittest

class MyTestCase(unittest.TestCase):
    
    def test_MakeLowercase(self):
        self.assertEqual(MakeLowercase("Masik"), "masik")
        self.assertEqual(MakeLowercase("F"),"f")
        with self.assertRaises(AttributeError):
            MakeLowercase(123)


