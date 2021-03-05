# -*- coding: utf-8 -*-

import os

from db_driver.write_db import write_db


def make_db():
    if not os.path.isfile("db.json"):
        write_db({})
