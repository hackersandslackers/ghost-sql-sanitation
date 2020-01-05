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
    return execute_sql_queries(db, queries)


def execute_sql_queries(db, queries):
    """Execute locally stored queries against remote database."""
    results = db.run_query(queries)
    return results
