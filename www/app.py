import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from alchemy import *
from config import local_db


app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = local_db
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
DPitems = Base.classes.dispatcher_phoenix


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        """Return the homepage."""
        return render_template("index.html")

@app.route("/features")
def features():
        return render_template("features.html")

@app.route("/dpmlquote/")
def smartQuote():
        return render_template("dpmlquote.html")


@app.route("/dpmsrenewal/", methods=["POST","GET"])
def mspostquote():
        if request.method == "POST":
                quote_id = insertMSQuote(request.form)
                return redirect(f"/dpmsrenewal/{quote_id}")
        if request.method == "GET":
                return render_template("dpmsrenewal.html")

@app.route("/dppkgquote/", methods=["POST", "GET"])
def postquote():
        if request.method == "POST":
                quote_id = insertQuote(request.form)
                return redirect(f"/dppkgquote/{quote_id}")
        if request.method == "GET":
                return render_template("dppkgquote.html")

@app.route("/dppkgquote/<quote_id>")
def getquote(quote_id):
    return render_template("dppkgquote-results.html")


@app.route("/dpmsrenewal/<quote_id>")
def getmsquote(quote_id):
        return render_template("dpmsrenewal-results.html")


@app.route("/dppkgquote/<quote_id>/json")
def quotedetail(quote_id):
    quote = getQuote(quote_id)
    return jsonify(quote)

@app.route("/dpmsrenewal/<quote_id>/json")
def msquotedetail(quote_id):
    quote = getMSQuote(quote_id)
    return jsonify(quote)

@app.route("/dispatcher/phoenix/editions")
def editions():
    results = getEditions()
    return jsonify(results)

@app.route("/dispatcher/phoenix/editions/<edition>")
def details(edition):
    results = getEditionDetails(edition)
    return jsonify(results)