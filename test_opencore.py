# test_opencore.py
"""
Tests for OpenCore module.
"""

import unittest
from opencore import OpenCore

class TestOpenCore(unittest.TestCase):
    """Test cases for OpenCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenCore()
        self.assertIsInstance(instance, OpenCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
