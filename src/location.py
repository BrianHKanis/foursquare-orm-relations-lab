import src
class Location:
    __table__ = 'locations'
    attributes = ['id', 'longitude', 'latitude', 'address', 
            'zipcode_id', 'venue_id', 'created_at']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def zipcode(self, cursor):
        query = """SELECT * FROM zipcodes JOIN
                    locations ON zipcodes.id = locations.zipcode_id
                    WHERE locations.id = %s"""
        cursor.execute(query, (self.id,))
        record = cursor.fetchone()
        zipcode_object = src.build_from_record(src.Zipcode, record)
        return zipcode_object
    
    def venue(self, cursor):
        query = """SELECT * FROM venues JOIN
                    locations on venues.id = locations.venue_id
                    WHERE locations.id = %s"""
        cursor.execute(query, (self.id,))
        record = cursor.fetchone()
        venue_object = src.build_from_record(src.Venue, record)
        return venue_object