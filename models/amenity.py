#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ public amenity class attributes """
    name = ""

    def __init__(self, *prmArg, **prmKwArg):
        """ Constructor """

        super().__init__(*prmArg, **prmKwArg)
