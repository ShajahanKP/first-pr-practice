import unittest

from textutils import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic_phrase(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_repeated_separators(self):
        self.assertEqual(slugify("a  --  b"), "a-b")

    def test_strips_leading_and_trailing_separators(self):
        self.assertEqual(slugify("  --Hello--  "), "hello")

    def test_keeps_digits(self):
        self.assertEqual(slugify("Version 2.0"), "version-2-0")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
