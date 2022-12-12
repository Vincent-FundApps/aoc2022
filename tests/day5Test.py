import unittest
import sys
sys.path.insert(1, '..')
import day5

class TestDay5(unittest.TestCase):
    def test_star1(self):        
        input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        d = day5.day5()
        self.assertEqual(d.star1(input), 'CMZ')
    
    def test_star2(self):        
        input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
        d = day5.day5()
        self.assertEqual(d.star2(input), 'MCD')


if __name__ == '__main__':
    unittest.main()
    TD = TestDay5()
    TD.test_star1()
    TD.test_star2()