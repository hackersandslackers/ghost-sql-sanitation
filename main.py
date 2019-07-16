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
    for query in queries:
        result = db.run_query(query)
    result = f"{len(queries)} queries successfully executed."
    return result
