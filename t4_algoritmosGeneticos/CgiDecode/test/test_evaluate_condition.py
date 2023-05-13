#!./venv/bin/python
import unittest
import sys
from src.evaluate_condition import evaluate_condition
from src.evaluate_condition import distances_true
from src.evaluate_condition import distances_false
from src.evaluate_condition import clear_maps


class TestEvaluateCondition(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testEqDifferentValues(self):
        result = evaluate_condition(1, "Eq", 10, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 10)
        self.assertEqual(distances_false[1], 0)

    def testEqSameValues(self):
        result = evaluate_condition(1, "Eq", 20, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def testNeDifferentValues(self):
        result = evaluate_condition(1, "Ne", 10, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 10)

    def testNeSameValues(self):
        result = evaluate_condition(1, "Ne", 20, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 1)
        self.assertEqual(distances_false[1], 0)

    def testLeLhsIsLower(self):
        result = evaluate_condition(1, "Le", 10, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 11)

    def testLeLhsIsNotLower(self):
        result = evaluate_condition(1, "Le", 20, 10)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 10)
        self.assertEqual(distances_false[1], 0)

    def testLeSameValue(self):
        result = evaluate_condition(1, "Le", 20, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def testLtLhsIsLower(self):
        result = evaluate_condition(1, "Lt", 10, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 10)

    def testGeLhsIsLarger(self):
        result = evaluate_condition(1, "Ge", 20, 10)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 11)

    def testGeLhsIsNotLarger(self):
        result = evaluate_condition(1, "Ge", 10, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 10)
        self.assertEqual(distances_false[1], 0)

    def testGeSameValue(self):
        result = evaluate_condition(1, "Ge", 20, 20)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def testGtLhsIsLarger(self):
        result = evaluate_condition(1, "Gt", 20, 10)
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 10)

    def testGtLhsIsNotLarger(self):
        result = evaluate_condition(1, "Gt", 10, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 11)
        self.assertEqual(distances_false[1], 0)

    def testGtSameValue(self):
        result = evaluate_condition(1, "Gt", 20, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 1)
        self.assertEqual(distances_false[1], 0)

    def test10NotInEmpty(self):
        result = evaluate_condition(1, "In", 10, [])
        self.assertFalse(result)
        self.assertEqual(distances_true[1], sys.maxsize)
        self.assertEqual(distances_false[1], 0)

    def test10NotInArray(self):
        result = evaluate_condition(1, "In", 10, [1,2,3])
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 7)
        self.assertEqual(distances_false[1], 0)

    def test10InArrayWith10(self):
        result = evaluate_condition(1, "In", 10, [10])
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def test10InArrayWithDuplicate10(self):
        result = evaluate_condition(1, "In", 10, [10,10])
        self.assertTrue(result)
        self.assertEqual(distances_true[1], 0)
        self.assertEqual(distances_false[1], 1)

    def test13NotInArrayWithNeighbourNumbers(self):
        result = evaluate_condition(1, "In", 13, [11,12,18])
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 1)
        self.assertEqual(distances_false[1], 0)

    def testEqDifferentValuesOverwritesValue(self):
        evaluate_condition(1, "Eq", 10, 20)
        result = evaluate_condition(1, "Eq", 11, 20)
        self.assertFalse(result)
        self.assertEqual(distances_true[1], 9)
        self.assertEqual(distances_false[1], 0)

    def testWithInvalidOperatorThrowsError(self):
        with self.assertRaises(ValueError):
            evaluate_condition(1, "EE", 10, 20)