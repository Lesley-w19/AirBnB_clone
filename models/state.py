#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    """ public state class attributes """
    name = ""

    def __init__(self, *prmArg, **prmKwArg):
        """ Constructor """
        super().__init__(*prmArg, **prmKwArg)
