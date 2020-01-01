"""Appliction entry point."""
from flask import Flask, make_response, jsonify
from .db import Database
from config import db_pem, db_uri, sql_folder
from .queries import read_sql_queries


def main(request):
    """Endpoint entry point."""
    db = Database(db_pem, db_uri)
    queries = read_sql_queries(sql_folder)
    results = [db.run_query(query) for query in queries]
    print(results)
    if request:
        return make_response(jsonify(results), 200)
