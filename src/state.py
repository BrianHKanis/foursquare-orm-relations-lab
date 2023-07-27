import src
class State:
    __table__ = 'states'
    attributes = ['id', 'name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    def cities(self, cursor):
        query = """SELECT * FROM cities WHERE state_id = %s"""
        cursor.execute(query, (self.id,))
        records = cursor.fetchall()
        city_objects = src.build_from_records(src.City, records)
        return city_objects