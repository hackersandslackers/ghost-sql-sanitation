import logging
from sqlalchemy import create_engine, MetaData



class Database:
    """Database connection class."""

    def __init__(self, db_pem, db_uri):
        self.engine = create_engine(db_uri,
                                    connect_args={'ssl': {'ca': db_pem}},
                                    echo=True)
        self.metadata = MetaData(bind=self.engine)

    def run_query(self, query):
        """Execute SQL query."""
        print(query)
        if 'SELECT' in query:
            results = self.engine.execute(query).fetchall()
            return self.__construct_response(len(results))
        results = self.engine.execute(query)
        return self.__construct_response(results.rowcount)

    @staticmethod
    def __construct_response(num_rows):
        """Summarize results of an executed query."""
        return f'Modified {num_rows} rows.'

