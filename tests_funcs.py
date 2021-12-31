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
        self.assertIsNone(funcs.mean({}))

    def test_median(self):
        self.assertEqual(funcs.median({3,1,4}),3)
        self.assertEqual(funcs.median({-2,-1,-4}),-2)
        self.assertEqual(funcs.median({1,3,4,5}),3.5)
        self.assertEqual(funcs.median({-1,-3,-7,-2}),-2.5)
        self.assertEqual(funcs.median({-1.2,3.6,4}),3.6)
        self.assertEqual(funcs.median({-1.2,3.6,4,2.6}),3.1)
        self.assertEqual(funcs.median({2}),2)
        self.assertIsNone(funcs.median({}))

    def test_st_dev(self):
        self.assertEqual(funcs.st_dev({2,4,6}),1.4142135623730951)
        self.assertIsNone(funcs.st_dev({}))


    def test_geo(self):
        self.assertFalse(funcs.geo([1]))
        self.assertTrue(funcs.geo([2,4,8]))
        self.assertFalse(funcs.geo([2,4,7]))

    def test_ari(self):
        self.assertFalse(funcs.ari([1]))
        self.assertTrue(funcs.ari([2,4,6]))
        self.assertFalse(funcs.ari([2,4,7]))

    def test_geo2(self):
        flag1, data_add1 = funcs.geo2([2,4,8],2)
        self.assertTrue(flag1)
        self.assertEqual(data_add1,[16, 32])

        flag1, data_add1 = funcs.geo2([2,4,7],2)
        self.assertFalse(flag1)
        self.assertEqual(data_add1,[])

    def test_ari2(self):
        flag1, data_add1 = funcs.ari2([2,4,6],2)
        self.assertTrue(flag1)
        self.assertEqual(data_add1,[8, 10])

        flag1, data_add1 = funcs.ari2([2,4,7],2)
        self.assertFalse(flag1)
        self.assertEqual(data_add1,[])
        

if __name__ == '__main__':
    unittest.main()