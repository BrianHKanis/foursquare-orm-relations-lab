DROP TABLE venues;
DROP TABLE locations;
DROP TABLE categories;
DROP TABLE venue_categories;

CREATE TABLE IF NOT EXISTS venues (
  id serial PRIMARY KEY,
  foursquare_id VARCHAR(255) UNIQUE,
  name VARCHAR(255) NOT NULL,
  price INTEGER,
  rating DECIMAL,
  likes BIGINT,
menu_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX venues_price_index ON venues (price);

CREATE TABLE IF NOT EXISTS locations (
  id serial PRIMARY KEY,
  longitude DECIMAL, 
   latitude DECIMAL, 
    address VARCHAR(255),
    postal_code INTEGER,
    city VARCHAR(255),
    state VARCHAR(255),
    venue_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    FOREIGN KEY (venue_id)
     REFERENCES venues (id)
  )
);

CREATE INDEX locations_postal_code_index ON locations (postal_code);
CREATE INDEX city_postal_code_index ON locations (city);
CREATE INDEX state_postal_code_index ON locations (state);

CREATE TABLE IF NOT EXISTS categories (
  id serial PRIMARY KEY,
  name VARCHAR(255) UNIQUE, 
);


CREATE TABLE IF NOT EXISTS venue_categories (
  id serial PRIMARY KEY,
  category_id INTEGER, 
  venue_id INTEGER, 
  FOREIGN KEY (category_id)
    REFERENCES categories (id)
  ),
  FOREIGN KEY (venue_id)
    REFERENCES venues (id)
  )
);




