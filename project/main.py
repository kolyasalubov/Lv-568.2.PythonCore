# ==============================================================
#                                                              #
#   keys:                                                      #
#                                                              #
#   name_of_the_company : " "                                  #
#   company_member_id :              where id is unique(time)  #
#       position : " "                                         #
#       name : " "                                             #
#       surname : " "                                          #
#       phone_number : " "                                     #
#                                                              #
# ==============================================================

# -*- coding: utf-8 -*-

from flask import Flask

from db_driver.make_db import make_db

from routes.index_route import index_route
from routes.add_member_route import add_member_route
from routes.add_company_route import add_company_route
from routes.edit_member_route import edit_member_route
from routes.edit_company_route import edit_company_route
from routes.delete_member_route import delete_member_route
from routes.delete_company_route import delete_company_route

make_db()

app = Flask("__name__")
app.register_blueprint(index_route)
app.register_blueprint(add_member_route)
app.register_blueprint(add_company_route)
app.register_blueprint(edit_member_route)
app.register_blueprint(edit_company_route)
app.register_blueprint(delete_member_route)
app.register_blueprint(delete_company_route)

if __name__ == "__main__":
    app.run(debug=True)
