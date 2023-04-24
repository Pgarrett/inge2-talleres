#!./venv/bin/python
import random
import unittest
from src.mutation_utils import insert_random_character, delete_random_character, flip_random_character


class TestMutationUtils(unittest.TestCase):

    def testDeleteInEmptyStringDoesNothing(self):
        s = delete_random_character("")
        self.assertEqual(s, "")

    def testDeleteInNonEmptyString(self):
        input = "Hello World"
        random.seed(2)
        s = delete_random_character(input)
        self.assertEqual(len(s), len(input) - 1)
        self.assertEqual(s, "ello World")

    def testModifyInEmptyStringDoesNothing(self):
        s = flip_random_character("")
        self.assertEqual(s, "")

    def testModifyInNonEmptyString(self):
        input = "Hello World"
        random.seed(2)
        s = flip_random_character(input)
        self.assertEqual(len(s), len(input))
        self.assertEqual(s, "lello World")

    def testInsertInNonEmptyString(self):
        input = "Hello World"
        random.seed(2)
        s = insert_random_character(input)
        self.assertEqual(len(s), len(input) + 1)
        self.assertEqual(s, "lHello World")

    def testInsertInEmptyString(self):
        input = ""
        random.seed(2)
        s = insert_random_character(input)
        self.assertEqual(len(s), len(input) + 1)
        self.assertEqual(s, "h")