import string
import unittest

from simu import random


__time__ = 100
__natural_range__ = [*range(0, random.DEFAULT_MAX + 1, 1)]
__integer_range__ = [*range(random.DEFAULT_MIN, random.DEFAULT_MAX + 1, 1)]


class RandomTest(unittest.TestCase):
    def test_boolean(self):
        for _ in range(__time__):
            self.assertIn(random.boolean(), [True, False])
            
    def test_booleans(self):
        bool_list = random.booleans()
        self.assertEqual(10, len(bool_list))
        for i in bool_list:
            self.assertIn(i, [True, False])
            
    def test_natural(self):
        for _ in range(__time__):
            self.assertIn(random.natural(), __natural_range__)
            
    def test_naturals(self):
        natural_list = random.naturals()
        self.assertEqual(10, len(natural_list))
        for i in natural_list:
            self.assertIn(i, __natural_range__)
            
    def test_integer(self):
        for _ in range(__time__):
            self.assertIn(random.integer(), __integer_range__)
            
    def test_integers(self):
        integer_list = random.integers()
        self.assertEqual(10, len(integer_list))
        for i in integer_list:
            self.assertIn(i, __integer_range__)
            
    def test_floating(self):
        for _ in range(__time__):
            self.assertTrue(random.floating() >= random.DEFAULT_MIN and random.floating() <= random.DEFAULT_MAX)
            
    def test_floatings(self):
        float_list = random.floatings()
        self.assertEqual(10, len(float_list))
        for i in float_list:
            self.assertTrue(random.floating() >= random.DEFAULT_MIN and random.floating() <= random.DEFAULT_MAX)
            
    def test_char(self):
        for _ in range(__time__):
            self.assertIn(random.char(), string.ascii_letters)
            
    def test_string(self):
        for _ in range(__time__):
            randstr = random.string()
            self.assertTrue(len(randstr) >= 3 and len(randstr) <= 10)
            
            
if __name__ == '__main__':
    unittest.main()