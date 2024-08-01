import subprocess

from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

from DataLoaderModule.code import load_data
from LoguruModule.code import LoguruDecoratorClass
from PostgresDBModule.code import PostgresDBClass

app = Flask(__name__)

load_dotenv(find_dotenv())


@LoguruDecoratorClass(level="INFO")
def get_db_connection():
    db = PostgresDBClass()
    return db


if __name__ == "__main__":
    load_data()