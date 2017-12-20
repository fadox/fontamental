import sys
import unittest
from fontamental.aragl import *


class IndexTest(unittest.TestCase):


    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        # self.infoTab = NameTabWidget(None)
        pass

    def tearDown(self):
        # self.fontInfo.close()
        pass

    def test_sample1(self):
        self.assertEqual(1, 1)

    def test_sample2(self):
        self.assertEqual(2, 2)


if __name__ == "__main__":
    unittest.main()
