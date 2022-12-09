import unittest
import sys
sys.path.insert(1, '..')
import day3

class TestDay3(unittest.TestCase):
    def test_star1(self):        
        input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        d3 = day3.day3()
        self.assertEqual(d3.star1(input), 157)
    
    def test_star2(self):
        input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
        d3 = day3.day3()
        self.assertEqual(d3.star2(input), 70)


if __name__ == '__main__':
    unittest.main()
    TD3 = TestDay3()
    TD3.test_star1()
    TD3.test_star2()