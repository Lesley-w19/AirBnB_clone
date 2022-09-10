#!/usr/bin/python3

""" Unittest for amenity.py """
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    rview = Review()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.rview)), res)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.rview, Review)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.rview, "place_id"))
        self.assertTrue(hasattr(self.rview, "user_id"))
        self.assertTrue(hasattr(self.rview, "text"))
        self.assertTrue(hasattr(self.rview, "id"))
        self.assertTrue(hasattr(self.rview, "created_at"))
        self.assertTrue(hasattr(self.rview, "updated_at"))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.rview.place_id, str)
        self.assertIsInstance(self.rview.user_id, str)
        self.assertIsInstance(self.rview.text, str)
        self.assertIsInstance(self.rview.id, str)
        self.assertIsInstance(self.rview.created_at, datetime.datetime)
        self.assertIsInstance(self.rview.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
