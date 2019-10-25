"""Appliction entry point."""
from flask import Flask, make_response, jsonify
from .db import Database
from config import Config
from .get_queries import read_sql_queries


def main(request):
    """Endpoint entry point."""
    config = Config()
    db = Database(config)
    queries = read_sql_queries(config.sql_folder)
    results = [db.run_query(query) for query in queries]
    print(results)
    if request:
        return make_response(jsonify(results), 200)
