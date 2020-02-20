"""Config values."""
from os import environ

db_user = environ.get('DATABASE_USERNAME')
db_password = environ.get('DATABASE_PASSWORD')
db_host = environ.get('DATABASE_HOST')
db_port = environ.get('DATABASE_PORT')
db_name = environ.get('DATABASE_NAME')
db_uri = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

db_cert = environ.get("DATABASE_CERT")
db_pem = environ.get("DATABASE_PEM")
db_key = environ.get("DATABASE_KEY")

# SQL queries
sql_folder = 'queries'
