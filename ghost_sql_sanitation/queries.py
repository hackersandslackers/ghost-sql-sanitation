"""Read SQL files."""
from sys import stdout
from os import listdir
from os.path import isfile, join
from loguru import logger

logger.add(stdout, format="{time} {message}", level="INFO")


class SQLFetcher:

    def __init__(self, folder):
        self.folder = folder

    def get_queries(self):
        """Neatly package local queries to be run against your database."""
        files = self.__fetch_sql_files()
        sql = self.__read_sql_queries(files)
        query_collection = dict(zip(files, sql))
        return query_collection

    def __fetch_sql_files(self):
        """Fetch all SQL query files in folder."""
        dir = listdir(self.folder)
        files = [self.folder + '/' + f for f in dir if isfile(join(self.folder, f)) if '.sql' in f]
        logger.info(f'Found {len(files)} queries from the `/queries` directory.')
        return files

    @staticmethod
    def __read_sql_queries(files):
        """Read SQL query from .sql file."""
        queries = []
        for file in files:
            fd = open(file, 'r')
            query = fd.read()
            queries.append(query)
            fd.close()
        return queries
