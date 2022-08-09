#!/usr/bin/python3

""" Unitest for user.py """

import unittest
from models.user import User
import datetime

class TestUser(unittest.TestCase):
    """ To tst the instances and methods from the user class """
    usr = User()

    def test_class_exists(self):
        """ if the class exists """
        self.assertEqual(str(type(self.usr)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """ if the user class is the subclass of BaseModel """
        self.assertIsInstance(self.usr, User)

    def test_has_attributes(self):
        """ to check for public user class atrributes """
        self.assertTrue(hasattr(self.usr, 'email'))
        self.assertTrue(hasattr(self.usr, 'password'))
        self.assertTrue(hasattr(self.usr, 'first_name'))
        self.assertTrue(hasattr(self.usr, 'last_name'))
        self.assertTrue(hasattr(self.usr, 'id'))
        self.assertTrue(hasattr(self.usr, 'created_at'))
        self.assertTrue(hasattr(self.usr, 'updated_at'))

    def test_types(self):
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.id, str)
        self.assertIsInstance(self.usr.created_at, datetime.datetime)
        self.assertIsInstance(self.usr.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
