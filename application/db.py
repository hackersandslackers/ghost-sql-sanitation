import logging
from sqlalchemy import create_engine, MetaData
from config import db_uri


logger = logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


class Database:
    """Database connection class."""

    engine = create_engine(db_uri,
                           connect_args={'sslmode': 'require'},
                           ssl_args={'ssl_ca': ca_path},
                           echo=True)
    metadata = MetaData(bind=engine)

    @classmethod
    def run_query(cls, query):
        """Execute SQL query."""
        results = cls.engine.execute(query)
        response = cls.__construct_response(len(results))
        return response

    def __construct_response(num_rows):
        """Summarize results of an executed query."""
        return f'Modified {num_rows} rows.'
