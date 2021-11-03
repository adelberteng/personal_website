-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS merchandise;
DROP TABLE IF EXISTS order;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  uid INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(32) UNIQUE NOT NULL,
  password_hash VARCHAR(128) NOT NULL
);

shopping cart system 
CREATE TABLE merchandise (
  merchandise_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  owner_id INTEGER NOT NULL,
  price INTEGER NOT NULL,
  stock INTEGER NOT NULL,
  created_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description TEXT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES user (uid)
);

CREATE TABLE order (
  order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  buyer_id INTEGER NOT NULL,
  merchanise_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (buyer_id) REFERENCES user (uid),
  FOREIGN KEY (merchandise_id) REFERENCES merchandise (merchandise_id)
);

-- reservation system
-- CREATE TABLE place (
--   place_id INTEGER PRIMARY KEY AUTOINCREMENT,
  
-- );

-- CREATE TABLE reservation (
--   reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  
-- );



-- blog system
-- CREATE TABLE post (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   author_id INTEGER NOT NULL,
--   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   title TEXT NOT NULL,
--   body TEXT NOT NULL,
--   FOREIGN KEY (author_id) REFERENCES user (id)
-- );
