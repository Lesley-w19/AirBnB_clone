#!/usr/bin/python3

from models.base_model from BaseModel

class Place(BaseModel):
    """ public place class attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *prmArg, **prmKwArg):
        """ constructor """
        super().__init__(*prmArg, **prmKwArg)