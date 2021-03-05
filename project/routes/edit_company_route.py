# -*- coding: utf-8 -*-

from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from db_driver.read_db import read_db
from db_driver.write_db import write_db


edit_company_route = Blueprint('edit_company_route', __name__)

@edit_company_route.route("/edit/company", methods=["POST", "GET"])
def edit_company():
    db_data = read_db()
    if "company" in db_data:
        if request.method == "GET":
            return render_template("/edit_company.html")
        else:
            name_of_the_company = request.form["name_of_the_company"]
            if name_of_the_company:
                db_data["company"]["name_of_the_company"] = name_of_the_company
                write_db(db_data)
        return redirect("/")
    else:
        return redirect("/add/company")
