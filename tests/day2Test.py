import unittest
import sys
sys.path.insert(1, '..')
import day2

class TestDay2(unittest.TestCase):
    def test_star1(self):        
        input = """A Y
B X
C Z"""
        d2 = day2.day2()
        self.assertEqual(d2.star1(input), 15)
    
    def test_star2(self):
        input = """A Y
B X
C Z"""
        d2 = day2.day2()
        self.assertEqual(d2.star2(input), 12)

if __name__ == '__main__':
    # unittest.main()
    TD2 = TestDay2()
    TD2.test_star1()
    TD2.test_star2()