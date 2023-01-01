import unittest
import sys
sys.path.insert(1, '..')
import day8

class Testday8(unittest.TestCase):
    def test_star1(self):        
        input = """30373
25512
65332
33549
35390"""
        d = day8.day8()
        self.assertEqual(d.star1(input), 21)


    def test_star2(self):        
        input = """30373
25512
65332
33549
35390"""
        d = day8.day8()
        self.assertEqual(d.star2(input), 8)



if __name__ == '__main__':
    unittest.main()
    TD = Testday8()
    TD.test_star1()
    TD.test_star2()