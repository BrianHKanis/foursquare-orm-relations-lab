import src
class City:
    __table__ = 'cities'
    attributes  = ['id', 'name', 'state_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def zipcodes(self, cursor):
        query = """SELECT * FROM zipcodes JOIN
                    cities on zipcodes.city_id = cities.id
                    WHERE cities.id = %s"""
        cursor.execute(query, (self.id,))
        records = cursor.fetchall()
        zipcode_objects = src.build_from_records(src.Zipcode, records)
        return zipcode_objects
    
    def state(self, cursor):
        query = """SELECT * from states JOIN
                    cities ON states.id = cities.state_id
                    WHERE cities.id = %s"""
        cursor.execute(query, (self.id,))
        record = cursor.fetchone()
        state_object = src.build_from_record(src.State, record)
        return state_object