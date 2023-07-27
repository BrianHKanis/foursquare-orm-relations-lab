import src
class Venue():
    __table__ = 'venues'
    attributes = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                raise f'{key} not in {self.attributes}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_foursquare_id(self, foursquare_id, cursor):
        foursquare_query = """SELECT * FROM venues WHERE foursquare_id = %s"""
        cursor.execute(foursquare_query, (foursquare_id,))
        record =  cursor.fetchone()
        return src.build_from_record(src.Venue, record)

    def location(self, cursor):
        query = """SELECT * FROM locations WHERE venue_id = %s"""
        cursor.execute(query, (self.id,))
        record = cursor.fetchone()
        location = src.Location()
        location_object = src.build_from_record(location.__class__, record)
        return location_object

    def categories(self, cursor):
        query = """SELECT * FROM categories JOIN
                    venue_categories ON categories.id = venue_categories.category_id
                    WHERE venue_categories.venue_id = %s"""
        cursor.execute(query, (self.id,))
        records = cursor.fetchall()
        category_objects = src.build_from_records(src.Category, records)
        return category_objects


