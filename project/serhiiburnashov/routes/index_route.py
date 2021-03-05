# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template

from db_driver.read_db import read_db
from db_driver.write_db import write_db

index_route = Blueprint('index_route', __name__)


@index_route.route("/")
def index():
    db_data = read_db()
    if "company" in db_data:
        main_text = db_data["company"]["name_of_the_company"]
        arr = db_data["company"]
    else:
        main_text = ""
        arr = {}
    return render_template("index.html", main_text=main_text, arr=arr)
