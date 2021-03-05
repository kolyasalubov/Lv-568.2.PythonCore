# -*- coding: utf-8 -*-

import json


def read_db():
    with open("db.json", "r") as read_file:
        data = json.load(read_file)
    return data
