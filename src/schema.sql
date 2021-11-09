DROP TABLE IF EXISTS user_tbl;
DROP TABLE IF EXISTS merchandise_tbl;
DROP TABLE IF EXISTS order_tbl;

CREATE TABLE user_tbl (
  uid INTEGER PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(32) UNIQUE NOT NULL,
  password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE merchandise_tbl (
  merchandise_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  owner_id INTEGER NOT NULL,
  price INTEGER NOT NULL,
  stock INTEGER NOT NULL,
  created_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description TEXT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES user_tbl (uid)
);

CREATE TABLE order_tbl (
  order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  buyer_id INTEGER NOT NULL,
  merchandise_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (buyer_id) REFERENCES user_tbl (uid),
  FOREIGN KEY (merchandise_id) REFERENCES merchandise_tbl (merchandise_id)
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
--   FOREIGN KEY (author_id) REFERENCES user_tbl (id)
-- );
