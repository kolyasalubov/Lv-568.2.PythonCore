# -*- coding: utf-8 -*-

from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from db_driver.read_db import read_db
from db_driver.write_db import write_db


add_company_route = Blueprint('add_company_route', __name__)

@add_company_route.route("/add/company", methods=["POST", "GET"])
def add_company():
    db_data = read_db()
    if "company" not in db_data:
        if request.method == "GET":
            return render_template("add_company.html")
        else:
            name_of_the_company = request.form["name_of_the_company"]
            if name_of_the_company:
                db_data["company"] = {
                    "name_of_the_company": name_of_the_company
                }
                write_db(db_data)
                return redirect("/")
            else:
                edit_style = "-error"
                return render_template("add_company.html", edit_style=edit_style)
