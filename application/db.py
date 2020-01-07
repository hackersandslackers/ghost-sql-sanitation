import sys
import pymysql
import logging
from sqlalchemy import create_engine, MetaData

class Database:
    """Database connection class."""

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.port = config.db_port
        self.dbname = config.db_name
        self.cert = config.db_cert
        self.key = config.db_key
        self.pem = config.db_pem
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        print(self.__dict__)
        if self.conn is None:
            try:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
            except pymysql.MySQLError as e:
                logging.error(e)
                sys.exit()

    def run_query(self, query):
        """Execute SQL query."""
        print(f"Running query: {query}")
        try:
            self.open_connection()
            with self.conn.cursor() as cursor:
                if 'SELECT' in query:
                    records = cursor.execute(query).fetchall()
                    cursor.close()
                    return records
                else:
                    cursor.execute(query)
                    self.conn.commit()
                    affected = f"{cursor.rowcount} rows affected."
                    cursor.close()
                    return affected
        except pymysql.MySQLError as e:
            print(e)
        finally:
            if self.conn is not None:
                self.conn.close()
