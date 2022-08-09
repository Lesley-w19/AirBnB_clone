#!/usr/bin/python3
""" unittest for state.py """

import unittest
import datetime
from models.state import State

class TestState(unittest.TestCase):
    """ tests the instances and methods of the state.py """
    ste = State()

    def state_class_exists(self):
        """ if the class exists """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.ste)), result)

    def test_state_inheritance(self):
        """ if state subclass inheris from the BaseModel """
        self.assertIsInstance(self.ste, State)

    def test_has_attributes(self):
        """ check for the public state class attributes """
        self.assertTrue(hasattr(self.ste, 'name'))
        self.assertTrue(hasattr(self.ste, 'id'))
        self.assertTrue(hasattr(self.ste, 'created_at'))
        self.assertTrue(hasattr(self.ste, 'updated_at'))

    def test_types(self):
        """ tests the type with attributes """
        self.assertIsInstance(self.ste.name, str)
        self.assertIsInstance(self.ste.id, str)
        self.assertIsInstance(self.ste.created_at, datetime.datetime)
        self.assertIsInstance(self.ste.updated_at, datetime.datetime)

if __name__ = '__main__':
    unittest.main()
