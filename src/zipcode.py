from src import *
from src.city import City
from src.location import Location
class Zipcode:
    __table__ = 'zipcodes'
    attributes = ['id', 'code', 'city_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def city(self, cursor):
        query = """SELECT * FROM cities JOIN
                    zipcodes ON cities.id = zipcodes.city_id
                    WHERE zipcodes.id = %s"""
        cursor.execute(query, (self.id,))
        record = cursor.fetchone()
        city = City()
        city_object = build_from_record(city.__class__, record)
        return city_object
    
    def locations(self, cursor):
        query = """SELECT * FROM locations JOIN
                    zipcodes ON locations.zipcode_id = zipcodes.id
                    WHERE zipcodes.id = %s"""
        cursor.execute(query, (self.id,))
        records = cursor.fetchall()
        location = Location()
        location_objects = build_from_records(location.__class__, records)
        return location_objects