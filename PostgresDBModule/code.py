import os

import psycopg2
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine

from LoguruModule.code import LoguruDecoratorClass

load_dotenv(find_dotenv())


class PostgresDBClass:
    def __init__(self):
        postgres_access_line = os.getenv('POSTGRES_ACCESS_LINE')
        if not postgres_access_line:
            raise ValueError("POSTGRES_ACCESS_LINE environment variable is not set")
        self.postgres_url = f"postgresql://{postgres_access_line}"
        self.engine = create_engine(self.postgres_url)

        load_dotenv(find_dotenv())
        self.conn = psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user='postgres',
            password=os.getenv('PASSWORD')
        )

    @LoguruDecoratorClass(level="INFO")
    def load_dataframe(self, dataframe, table_name, if_exists='replace', index=False, dtype=None):
        dataframe.to_sql(table_name, self.engine, if_exists=if_exists, index=index, dtype=dtype)

    @LoguruDecoratorClass(level="INFO")
    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    @LoguruDecoratorClass(level="INFO")
    def close(self):
        self.conn.close()

    @LoguruDecoratorClass(level="INFO")
    def check_table_exists(self, table_name):
        query = f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = '{table_name}'
        );
        """
        result = self.execute_query(query)
        return result[0][0]
