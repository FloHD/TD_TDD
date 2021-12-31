import funcs
import unittest



class TestFuncs(unittest.TestCase):

    def test_min_int(self):
        self.assertEqual(funcs.min_int(0,2),0)
        self.assertEqual(funcs.min_int(-1,-5),-5)
        self.assertEqual(funcs.min_int(-1,2),-1)
        self.assertEqual(funcs.min_int(0,0),0)

    def test_mean(self):
        self.assertEqual(funcs.mean({2,3,4}),3)
        self.assertEqual(funcs.mean({-2,-3,-4}),-3)
        self.assertEqual(funcs.mean({-2,2,2,-2}),0)
        self.assertEqual(funcs.mean({-1.2,3.6,4}),(-1.2 + 3.6 + 4) / 3.0)
        self.assertEqual(funcs.mean({2}),2)
        self.assertEqual(funcs.mean({}),None)

    def test_median(self):
        self.assertEqual(funcs.median({3,1,4}),3)
        self.assertEqual(funcs.median({-2,-1,-4}),-2)
        self.assertEqual(funcs.median({1,3,4,5}),3.5)
        self.assertEqual(funcs.median({-1,-3,-7,-2}),-2.5)
        self.assertEqual(funcs.median({-1.2,3.6,4}),3.6)
        self.assertEqual(funcs.median({-1.2,3.6,4,2.6}),3.1)
        self.assertEqual(funcs.median({2}),2)
        self.assertEqual(funcs.median({}),None)

    def test_st_dev(self):
        self.assertEqual(funcs.st_dev({2,4,6}),1.4142135623730951)
        self.assertEqual(funcs.st_dev({}),None)

if __name__ == '__main__':
    unittest.main()