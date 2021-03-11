# -*- coding: utf-8 -*-

from flask import redirect
from flask import Blueprint

from db_driver.read_db import read_db
from db_driver.write_db import write_db


delete_company_route = Blueprint('delete_company_route', __name__)

@delete_company_route.route("/delete/company")
def delete_company():
    db_data = read_db()
    db_data.pop("company")
    write_db(db_data)
    return redirect("/")
