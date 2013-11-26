# -*- coding: utf-8 -*-
"""
Exif compare unit tests.
"""
import unittest

from exif_compare import main


# pylint: disable=E1103
class ExifCompareViewsTestCase(unittest.TestCase):
    """
    Views tests.
    """

    def setUp(self):
        """
        Before each test, set up a environment.
        """
        self.client = main.app.test_client()

    def tearDown(self):
        """
        Get rid of unused objects after each test.
        """
        pass

    def test_mainpage(self):
        """
        Test main page redirect.
        """
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class ExifCompareUtilsTestCase(unittest.TestCase):
    """
    Utility functions tests.
    """

    def setUp(self):
        """
        Before each test, set up a environment.
        """
        pass

    def tearDown(self):
        """
        Get rid of unused objects after each test.
        """
        pass


def suite():
    """
    Default test suite.
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExifCompareViewsTestCase))
    suite.addTest(unittest.makeSuite(ExifCompareUtilsTestCase))
    return suite


if __name__ == '__main__':
    unittest.main()
