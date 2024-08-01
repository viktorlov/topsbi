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


@app.route('/')
def index():
    db = get_db_connection()
    table_exists = db.check_table_exists('joined')

    if table_exists:
        query = f"""
        SELECT "Name_plm", "oboznachenie_421975", "Name_Classes" 
        FROM joined
        WHERE "oboznachenie_421975" IS NOT NULL
        """
        items = db.execute_query(query)
        db.close()
        return render_template('index.html', items=items)
    else:
        db.close()
        return "Table 'joined' does not exist. Run 2_generateJoinedTable"


if __name__ == "__main__":
    app.run(debug=False)
