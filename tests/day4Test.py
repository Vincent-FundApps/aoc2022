import unittest
import sys
sys.path.insert(1, '..')
import day4

class TestDay4(unittest.TestCase):
    def test_star1(self):        
        input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        d = day4.day4()
        self.assertEqual(d.star1(input), 2)
    
    def test_star2(self):
        input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
        d = day4.day4()
        self.assertEqual(d.star2(input), 4)


if __name__ == '__main__':
    unittest.main()
    TD = TestDay4()
    TD.test_star1()
    TD.test_star2()