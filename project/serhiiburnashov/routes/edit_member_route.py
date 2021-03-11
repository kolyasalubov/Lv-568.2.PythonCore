# -*- coding: utf-8 -*-

import re
from flask import request
from flask import redirect
from flask import Blueprint
from flask import render_template

from db_driver.read_db import read_db
from db_driver.write_db import write_db

edit_member_route = Blueprint('edit_member_route', __name__)


@edit_member_route.route("/edit/<string:item>", methods=["POST", "GET"])
def edit_member(item):
    db_data = read_db()
    if request.method == "GET":
        return render_template("edit_member.html")
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
                return render_template("edit_member.html", error_phone=error_phone)
        if member_data != {}:
            for i in member_data:
                db_data["company"][item][i] = member_data[i]
                write_db(db_data)
    return redirect("/")
