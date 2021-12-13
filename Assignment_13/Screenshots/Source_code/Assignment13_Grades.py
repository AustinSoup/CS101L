########################################################################
##
## CS 101 Lab
## Program # 13
## Name:Austin Souphanh
## Email: ajs2dz@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import unittest
import grades


class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")


    def test_total_returns_0(self):
        result = grades.total([])
        self.assertEqual(result, 0, "The total function should return 0")

class SimpleTest(unittest.TestCase):

    def test_average_one(self):
        values = (2,5,9)
        self.assertAlmostEqual(grades.average(values),5.33333,5)
  
    def test_average_two(self):
        values = (2,15,22,9)
        self.assertAlmostEqual(grades.average(values),12.0000,4)

    def test_average_returns_nan(self):
        values = ()
        self.assertIs(grades.average(values), math.nan)

class SimpleTest(unittest.TestCase):
    
    def test_median_a(self):
        result = grades.median([2,5,1])
        self.assertEqual(result,2,)
    
    def test_median_b(self):
        result = grades.median([5,2,1,3])
        self.assertEqual(result,2.5)

    def test_median_returns_ValueError(self):
        with self.assertRaises(ValueError):
            result = grades.median([])
            

unittest.main()
