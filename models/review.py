#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """public review class attributes"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *prmArg, **prmKwArg):
        """Constructor"""
        super().__init__(*prmArg, **prmKwArg)
