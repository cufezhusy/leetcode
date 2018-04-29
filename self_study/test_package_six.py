# Six provides simple utilities for wrapping over differences between Python 2 and Python 3.
# It is intended to support codebases that work on both Python 2 and 3 without modification.
# six consists of only one Python file, so it is painless to copy into a project.
# test
import six
import unittest


# Six contains compatibility shims for unittest assertions that have been renamed. The parameters are the same
#  as their aliases, but you must pass the test method as the first argument. For example:
class TestAssertCountEqual(unittest.TestCase):
    def test(self):
        six.assertCountEqual(self, (1, 2), [2, 1])

    def test_2(self):
        six.assertCountEqual(self, (1, 3), [3, 1])
class TestDataType(unittest.TestCase):
    def test(self):
        self.assertEqual(isinstance(6, six.integer_types),True)
        self.assertEqual(isinstance(6.6, six.integer_types), False)
        self.assertEqual(isinstance("shengyao", six.string_types),True)
        self.assertEqual(isinstance('shengyao', six.string_types), True)
