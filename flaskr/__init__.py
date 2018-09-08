#!/usr/bin/python3
# -*- coding: latin-1 -*-
import os
import sys
import psycopg2
import json
# from bson import json_util
# from pymongo import MongoClient
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

# REPLACE WITH YOUR DATABASE NAME
""" MONGODATABASE = "myDatabase"
MONGOSERVER = "localhost"
MONGOPORT = 27017
client = MongoClient(MONGOSERVER, MONGOPORT)
mongodb = client[MONGODATABASE]
"""
''' # Uncomment for postgres connection
# REPLACE WITH YOUR DATABASE NAME, USER AND PASS
POSTGRESDATABASE = "mydatabase"
POSTGRESUSER = "myuser"
POSTGRESPASS = "mypass"
postgresdb = psycopg2.connect(
    database=POSTGRESDATABASE,
    user=POSTGRESUSER,
    password=POSTGRESPASS)
'''

#Cambiar por Path Absoluto en el servidor
QUERIES_FILENAME = 'queries'


@app.route("/")
def home():
	return "Hellp world"




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
