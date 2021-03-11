# -*- coding: utf-8 -*-

import json


def write_db(data):
    with open("db.json", "w") as write_file:
        json.dump(data, write_file, indent=4)
