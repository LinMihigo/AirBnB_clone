#!/usr/bin/python3
"""
Unit tests for the BaseModel Class

Test methods:
    test_instance_creation:
        Tests instance creation

"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

if __name__ == "__main__":
    unittest.main()
