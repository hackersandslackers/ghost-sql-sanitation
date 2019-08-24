"""Appliction entry point."""
from flask import Flask, make_response, request, jsonify
from db import Database
from config import Config
from sql import read_sql


def main(request):
    """Endpoint entry point."""
    config = Config()
    db = Database(config)
    queries = read_sql(config.sql_folder)
    results = [db.run_query(query) for query in queries]
    print(results)
    # return jsonify(results)


main(1)
