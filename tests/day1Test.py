import unittest
import sys
sys.path.insert(1, '..')
import day1

class TestDay1(unittest.TestCase):
    def star1(self):        
        input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        d1 = day1.day1()
        self.assertEqual(d1.star1(input), 24000)
    
    def star2(self):
        input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
        d1 = day1.day1()
        d1.star1(input)
        self.assertEqual(d1.star2(), 45000)

if __name__ == '__main__':
    TD1 = TestDay1()
    TD1.star1()
    TD1.star2()