"""Appliction entry point."""
from flask import Flask, make_response, jsonify
from .database import Database
from config import db_pem, db_uri, sql_folder
from .queries import SQLFetcher


def main(request):
    """Endpoint entry point."""
    db = Database(db_pem, db_uri)
    fetcher = SQLFetcher(sql_folder)
    queries = fetcher.get_queries()
    results = db.run_query(queries)
    return make_response(jsonify(results), 200)
