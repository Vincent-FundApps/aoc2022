import unittest
import sys
sys.path.insert(1, '..')
import day6

class TestDay6(unittest.TestCase):
    def test_star1_1(self):        
        input = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
        d = day6.day6()
        self.assertEqual(d.star1(input), 5)

    def test_star1_2(self):        
        input = """nppdvjthqldpwncqszvftbrmjlhg"""
        d = day6.day6()
        self.assertEqual(d.star1(input), 6)
    
    def test_star1_3(self):        
        input = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
        d = day6.day6()
        self.assertEqual(d.star1(input), 10)

    def test_star1_4(self):        
        input = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""
        d = day6.day6()
        self.assertEqual(d.star1(input), 11)
    
    def test_star2_1(self):        
        input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
        d = day6.day6()
        self.assertEqual(d.star2(input), 19)



if __name__ == '__main__':
    unittest.main()
    TD = TestDay6()
    TD.test_star1_1()
    TD.test_star1_2()
    TD.test_star1_3()
    TD.test_star1_4()
    TD.test_star2_1()