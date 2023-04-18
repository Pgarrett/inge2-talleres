#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode


class TestCgiDecode(unittest.TestCase):
    def testSimple(self):
        decoded = cgi_decode("Hello World")
        self.assertEqual(decoded, "Hello World")

    def testWithPlus(self):
        decoded = cgi_decode("H+o")
        self.assertEqual(decoded, "H o")

    def testWithEscapedValue(self):
        decoded = cgi_decode("H%2F")
        self.assertEqual(decoded, "H/")

    def testWithHalfEscapedThrowsError(self):
        with self.assertRaises(ValueError):
            cgi_decode("H%2G")