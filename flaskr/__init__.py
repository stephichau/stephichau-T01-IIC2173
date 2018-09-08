#!/usr/bin/python3
# -*- coding: latin-1 -*-
import os
import sys
import psycopg2
from flask import Flask, request, redirect, render_template, url_for
from datetime import datetime as dt

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
def home(message=None):
	return render_template('index.html', message=message)

@app.route("/commentaries")
def get_commentaries():
    cur = postgresdb.cursor()
    cur.execute('SELECT * FROM commentary')
    results = []
    data = cur.fetchone()
    while data:
        results.append(data)
        data = cur.fetchone()
    results.reverse()
    return render_template('search.html', results=results, search='')

@app.route("/post", methods=["POST"])
def post_comment():
    cur = postgresdb.cursor()
    TO_ADD = request.form["text"]
    if len(TO_ADD) != 1 and "DROP" not in TO_ADD:
        TIMESTAMP = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        IP_ADDR = request.remote_addr
        consult = f'insert into commentary(ip, date, text) values(%s, %s, %s)'

        cur.execute(consult, (IP_ADDR, TIMESTAMP, TO_ADD, ))
        postgresdb.commit()
        return redirect(url_for('get_commentaries'))
    else:
        return home(message="Mensaje no puede estar vacio")


if __name__ == "__main__":
    app.run()
