from solution import Solution
import unittest
from ast import literal_eval

class TestSolution(unittest.TestCase):
    def test_solution(self):
        with open('6-22-2023/testcases.txt') as ifile: 
            for iline in ifile:
                with self.subTest(line=iline):
                    pass
                    # iline = iline.strip("\n")
                    # lineList = iline.split(", ")
                    # self.assertEqual(Solution.isValid(self, literal_eval(lineList[0])), literal_eval(lineList[1]))

if __name__ == '__main__':
    unittest.main()