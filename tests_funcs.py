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
        self.assertEqual(funcs.mean({-1.2,3.6,4}),(-1.2 + 3.6 + 4) / 3)
        self.assertEqual(funcs.mean({1}),1)

if __name__ == '__main__':
    unittest.main()