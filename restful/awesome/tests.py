__author__ = 'rrmerugu'


import unittest

def smile():
    return ":)"

def frown():
    return ":("


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(smile(), ":)")


if __name__ == '__main__':
    unittest.main()