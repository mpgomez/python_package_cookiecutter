"""Test the main module."""
from {{ cookiecutter.module_name }} import {{ cookiecutter.module_name }}
import sys
import unittest

class TestDemo(unittest.TestCase):
    def test_main(self):
        sys.argv = ["", ""]
        {{ cookiecutter.module_name}}.main()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

