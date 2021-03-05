# -*- coding: utf-8 -*-

from flask import redirect
from flask import Blueprint

from db_driver.read_db import read_db
from db_driver.write_db import write_db

delete_member_route = Blueprint('delete_member_route', __name__)


@delete_member_route.route("/delete/<string:item>")
def delete_member(item):
    db_data = read_db()
    db_data["company"].pop(item)
    write_db(db_data)
    return redirect("/")
