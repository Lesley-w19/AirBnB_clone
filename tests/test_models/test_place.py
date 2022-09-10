#!/usr/bin/python3
""" Unittest for plce.py """

import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests instances and methods from place class"""

    plce = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.plce)), "<class 'models.place.Place'>")

    def test_place_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.plce, Place)

    def testHasAttributes(self):
        """verify if publice place class attributes exist"""
        self.assertTrue(hasattr(self.plce, 'city_id'))
        self.assertTrue(hasattr(self.plce, 'user_id'))
        self.assertTrue(hasattr(self.plce, 'name'))
        self.assertTrue(hasattr(self.plce, 'description'))
        self.assertTrue(hasattr(self.plce, 'number_rooms'))
        self.assertTrue(hasattr(self.plce, 'number_bathrooms'))
        self.assertTrue(hasattr(self.plce, 'max_guest'))
        self.assertTrue(hasattr(self.plce, 'price_by_night'))
        self.assertTrue(hasattr(self.plce, 'latitude'))
        self.assertTrue(hasattr(self.plce, 'longitude'))
        self.assertTrue(hasattr(self.plce, 'amenity_ids'))
        self.assertTrue(hasattr(self.plce, 'id'))
        self.assertTrue(hasattr(self.plce, 'created_at'))
        self.assertTrue(hasattr(self.plce, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.plce.city_id, str)
        self.assertIsInstance(self.plce.user_id, str)
        self.assertIsInstance(self.plce.name, str)
        self.assertIsInstance(self.plce.description, str)
        self.assertIsInstance(self.plce.number_rooms, int)
        self.assertIsInstance(self.plce.number_bathrooms, int)
        self.assertIsInstance(self.plce.max_guest, int)
        self.assertIsInstance(self.plce.price_by_night, int)
        self.assertIsInstance(self.plce.latitude, float)
        self.assertIsInstance(self.plce.longitude, float)
        self.assertIsInstance(self.plce.amenity_ids, list)
        self.assertIsInstance(self.plce.id, str)
        self.assertIsInstance(self.plce.created_at, datetime.datetime)
        self.assertIsInstance(self.plce.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
