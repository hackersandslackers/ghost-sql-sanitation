from flask import Flask, make_response, jsonify
from flask import current_app as app
from ghost_sql_sanitation.queries import SQLFetcher
from config import sql_folder


def run_queries(db):
    fetcher = SQLFetcher(sql_folder)
    queries = fetcher.get_queries()
    results = db.run_query(queries)
    return make_response(jsonify(results), 200)
