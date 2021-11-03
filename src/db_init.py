# run this script after docker-compose
# initialization the database tables
# sql table schema refer to /src/schema.sql

import typing as t

from sqlalchemy import create_engine

from web.config import Config
conf = Config.load(env="dev")

database = conf.get("MYSQL_DATABASE")
mysql_user = conf.get("MYSQL_USER")
mysql_password = conf.get("MYSQL_PASSWORD")
mysql_endpoint = "localhost"
mysql_port = 3306
secret_key = conf.get("secret_key")

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{mysql_user}:{mysql_password}@"
    f"{mysql_endpoint}:{mysql_port}/{database}"
)

db = create_engine(SQLALCHEMY_DATABASE_URI)

def drop_table(table_name: str) -> None:
    db.execute(f"DROP TABLE IF EXISTS {table_name};")

def show_table() -> t.List[t.Tuple]:
    res = db.execute("SHOW TABLES;").fetchall()

    return res

def create_user_tbl() -> None:
    sql_text = """
        CREATE TABLE user_tbl (
        uid INTEGER PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(32) UNIQUE NOT NULL,
        password_hash VARCHAR(128) NOT NULL
        );
    """
    db.execute(sql_text)

def create_merchandise_tbl() -> None:
    sql_text = """
        CREATE TABLE merchandise_tbl (
        merchandise_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        owner_id INTEGER NOT NULL,
        price INTEGER NOT NULL,
        stock INTEGER NOT NULL,
        created_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        FOREIGN KEY (owner_id) REFERENCES user_tbl (uid)
        );
    """
    db.execute(sql_text)

def create_order_tbl() -> None:
    sql_text = """
        CREATE TABLE order_tbl (
        order_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        buyer_id INTEGER NOT NULL,
        merchandise_id INTEGER NOT NULL,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (buyer_id) REFERENCES user_tbl (uid),
        FOREIGN KEY (merchandise_id) REFERENCES merchandise_tbl (merchandise_id)
        );
    """
    db.execute(sql_text)


if __name__ == "__main__":
    drop_table("order_tbl")
    drop_table("merchandise_tbl")
    drop_table("user_tbl")
    create_user_tbl()
    create_merchandise_tbl()
    create_order_tbl()




