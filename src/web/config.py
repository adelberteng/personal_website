import os
from configparser import ConfigParser

class Config:
	""" Make default dir and env forward to the config"""
	_default_env = "dev"
	_top_dir_path = os.path.dirname(
		os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	_default_conf_path = os.path.join(_top_dir_path, "conf/config.ini")

	@staticmethod
	def load(env= _default_env, path= _default_conf_path):
		config = ConfigParser()
		config.read(path, encoding='utf-8')

		return config[env]