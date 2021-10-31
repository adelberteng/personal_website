import os
from configparser import ConfigParser

class Config:
	__TOP_DIR_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	__DEFAULT_CONF_PATH = os.path.join(__TOP_DIR_PATH, "conf/config.ini")

	__DEFAULT_ENV = "dev" 

	@staticmethod
	def load(env=__DEFAULT_ENV, path=__DEFAULT_CONF_PATH):
		config = ConfigParser()
		config.read(path, encoding='utf-8')

		return config[env]


if __name__ == '__main__':
	config = Config.load(env="dev")
	print(config["MYSQL_DATABASE"])