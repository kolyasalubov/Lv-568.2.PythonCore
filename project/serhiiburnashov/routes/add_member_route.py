# -*- coding: utf-8 -*-

import re
from time import time
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from db_driver.read_db import read_db
from db_driver.write_db import write_db

add_member_route = Blueprint('add_member_route', __name__)


@add_member_route.route("/add/member", methods=["POST", "GET"])
def add_member():
    db_data = read_db()
    if request.method == "GET":
        return render_template("add_member.html")
    else:
        member_data = {}
        if request.form["position"]:
            member_data["position"] = request.form["position"]
        if request.form["name"]:
            member_data["name"] = request.form["name"]
        if request.form["surname"]:
            member_data["surname"] = request.form["surname"]
        if request.form["phone_number"]:
            edit_phone_number = request.form["phone_number"]
            edit_phone_number.isdigit()
            if edit_phone_number.isdigit() and len(edit_phone_number) == 12:
                edit_phone_number = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{2})(\d{2})',
                                           r'+\1(\2)\3-\4-\5', edit_phone_number)
                member_data["phone_number"] = edit_phone_number
            else:
                error_phone = "border: 1px solid #ff0000"
                return render_template("add_member.html", error_phone=error_phone)
        if "position" in member_data and "name" in member_data and "phone_number" in member_data:
            id_timestamp = ''.join(str(time()).split("."))
            db_data["company"][f"company_member_{str(id_timestamp)}"] = member_data
        else:
            edit_style = "-error"
            return render_template("add_member.html", edit_style=edit_style)
        write_db(db_data)
    return redirect("/")
