"""Appliction entry point."""
from flask import Flask
from config import db_pem, db_uri, sql_folder
from .database import Database


db = Database(db_pem, db_uri)


def main(request):
    """Script entry point."""
    app = Flask(__name__)
    with app.app_context():
        from .run import run_queries

        return run_queries(db)
