#from pytest import *
from unittest import TestCase
from hello import NameExtractor

class TestNameExtractor(TestCase):
    def test_TestTwo(self):
        Steve1 = NameExtractor("Steven Kha")
        Steve1.ParseName()
        print(len(Steve1.mWords))

        self.assertEquals("", Steve1.mTitle)
        self.assertEqual("Steven", Steve1.mFirstName)
        self.assertEquals("", Steve1.mMiddleName)
        #self.assertIsNone(Steve1.mMiddleName, None)
        self.assertEqual("Kha", Steve1.mLastName)
        self.assertEqual("", Steve1.mSuffix)


        Steve2 = NameExtractor("Mr. Steven Kha")
        self.assertEqual("Mr", Steve2.mTitle)
        self.assertEqual("Steven", Steve2.mFirstName)
        self.assertEqual("", Steve2.mMiddleName)
        self.assertEqual("Kha", Steve2.mLastName)
        self.assertEqual("", Steve2.mSuffix)

        Steve3 = NameExtractor("Steven Kha, PhD")
        self.assertEqual("Steven", Steve3.mFirstName)
        self.assertEqual("Kha", Steve3.mLastName)
        self.assertEqual("PhD", Steve3.mSuffix)

