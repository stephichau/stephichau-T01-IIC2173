#!/usr/bin/python3
# -*- coding: latin-1 -*-
import os
import sys
import psycopg2
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from params import POSTGRESDATABASE, POSTGRESPASS, POSTGRESUSER

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

postgresdb = psycopg2.connect(
    database=POSTGRESDATABASE,
    user=POSTGRESUSER,
    password=POSTGRESPASS)


@app.route("/")
def home():
	return "Hellp world"

@app.route("/commentaries")
    return "All comments"

@app.route("/postgres")
def postgres():
    query = request.args.get("query")
    cursor = postgresdb.cursor()
    cursor.execute(query)
    results = [[a for a in result] for result in cursor]
    print(results)
    return render_template('postgres.html', results=results)


@app.route("/example")
def example():
    return render_template('example.html')


if __name__ == "__main__":
    app.run()
