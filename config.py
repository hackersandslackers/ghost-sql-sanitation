"""Config values."""
from os import environ

db_user = environ.get('DATABASE_USERNAME')
db_password = environ.get('DATABASE_PASSWORD')
db_host = environ.get('DATABASE_HOST')
db_port = environ.get('DATABASE_PORT')
db_name = environ.get('DATABASE_NAME')
db_connector = 'mysql+pymysql'
db_uri = f'{db_connector}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# SQL queries
sql_folder = environ.get('SQL_FOLDER')
