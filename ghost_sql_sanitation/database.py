from sys import stdout
from sqlalchemy import create_engine, MetaData
from loguru import logger

logger.add(stdout, format="{time} {message}", level="INFO")


class Database:
    """Database connection class."""

    def __init__(self, db_pem, db_uri):
        self.engine = create_engine(db_uri,
                                    connect_args={'ssl': {'ca': db_pem}},
                                    echo=False)
        self.metadata = MetaData(bind=self.engine)

    def run_query(self, sql_queries):
        """Execute SQL query."""
        affected_rows = 0
        for k, v in sql_queries.items():
            logger.info(f'Executing query: {k}')
            if 'SELECT' in v:
                results = self.engine.execute(v).fetchall()
                affected_rows = len(results)
            results = self.engine.execute(v)
            affected_rows = results.rowcount
            logger.info(f'Modified {affected_rows} rows.')
        return affected_rows

    @staticmethod
    def __construct_response(num_rows):
        """Summarize results of an executed query."""
        return f'Modified {num_rows} rows.'
