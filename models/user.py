#!/usr/bin/python3
""" a class User that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """public class attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *prmArg, **prmKwArg):
        """constructor"""

        super().__init__(*prmArg, **prmKwArg)
