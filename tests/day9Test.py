import unittest
import sys
sys.path.insert(1, '..')
import day9

class Testday9(unittest.TestCase):
    def test_star1(self):        
        input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        d = day9.day9()
        self.assertEqual(d.star1(input), 13)


    def test_star2(self):        
        input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
        d = day9.day9()
        self.assertEqual(d.star2(input), 36)



if __name__ == '__main__':
    unittest.main()
    TD = Testday9()
    TD.test_star1()
    # TD.test_star2()