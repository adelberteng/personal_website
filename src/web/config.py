import os
from datetime import timedelta
from configparser import ConfigParser

class Config:
    """ Read configuration from config.ini """
    _default_env = "dev"
    _top_dir_path = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    _default_conf_path = os.path.join(_top_dir_path, "conf/config.ini")

    @staticmethod
    def load(env= _default_env, path= _default_conf_path):
        config = ConfigParser()
        config.read(path, encoding='utf-8')

        return config[env]

conf = Config.load(env="dev")

database = conf.get("MYSQL_DATABASE")
mysql_user = conf.get("MYSQL_USER")
mysql_password = conf.get("MYSQL_PASSWORD")
mysql_endpoint = "app_network"
mysql_port = 3306
secret_key = conf.get("secret_key")

class AppConfig:
    """ make flask app get config from object """
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{mysql_user}:{mysql_password}@"
        f"{mysql_endpoint}:{mysql_port}/{database}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secret_key
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
