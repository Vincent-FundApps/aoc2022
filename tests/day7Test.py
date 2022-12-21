import unittest
import sys
sys.path.insert(1, '..')
import day7

class Testday7(unittest.TestCase):
    def test_star1(self):        
        input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        d = day7.day7()
        self.assertEqual(d.star1(input), 95437)


    def test_star2(self):        
        input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
        d = day7.day7()
        self.assertEqual(d.star2(input), 24933642)



if __name__ == '__main__':
    unittest.main()
    TD = Testday7()
    TD.test_star1()
    TD.test_star2()