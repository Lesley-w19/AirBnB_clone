#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """public city class attributes"""

    state_id = ""
    name = ""

    def __init__(self, *prmArg, **prmKwArg):
        """constructor"""

        super().__init__(*prmArg, **prmKwArg)
