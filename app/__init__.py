"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pm64dadc9vlvsr10-a.oregon-postgres.render.com",
        database="todo_ynxb",
        user="root",
        password="wObXdHGlF7szzbqDzFlAmFtSvNwCYiIN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
