#!./venv/bin/python
import unittest
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import distances_true
from src.evaluate_condition import distances_false
from src.evaluate_condition import clear_maps


class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testSimpleHelloReader(self):
        decoded = cgi_decode_instrumented("Hello+Reader")
        self.assertEqual(decoded, "Hello Reader")
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_true[2], 0)
        self.assertEqual(distances_true[3], 35)
        self.assertEqual(distances_false[1], 0)
        self.assertEqual(distances_false[2], 0)
        self.assertEqual(distances_false[3], 0)

    def testWithPlus(self):
        decoded = cgi_decode_instrumented("H o")
        self.assertEqual(decoded, "H o")
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_true[2], 11)
        self.assertEqual(distances_true[3], 5)
        self.assertEqual(distances_false[1], 0)
        self.assertEqual(distances_false[2], 0)
        self.assertEqual(distances_false[3], 0)

    def testWithEscapedValue(self):
        decoded = cgi_decode_instrumented("H%2F")
        self.assertEqual(decoded, "H/")
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_true[2], 6)
        self.assertEqual(distances_true[3], 0)
        self.assertEqual(distances_false[1], 0)
        self.assertEqual(distances_false[2], 0)
        self.assertEqual(distances_false[3], 0)
