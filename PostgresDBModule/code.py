import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, MetaData

from LoguruModule.code import LoguruDecoratorClass

load_dotenv(find_dotenv())


class PostgresDBClass:
    """
    Класс для работы с базой данных PostgreSQL.
    Использует SQL Alchemy для записи исторических и текущих данных криптовалют в БД.
    """

    def __init__(self):
        postgres_access_line = os.getenv('POSTGRES_ACCESS_LINE')
        if not postgres_access_line:
            raise ValueError("POSTGRES_ACCESS_LINE environment variable is not set")
        self.postgres_url = f"postgresql://{postgres_access_line}"
        self.engine = create_engine(self.postgres_url)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    @LoguruDecoratorClass(level="INFO")
    def load_dataframe(self, dataframe, table_name, if_exists='replace', index=False, dtype=None):
        dataframe.to_sql(table_name, self.engine, if_exists=if_exists, index=index, dtype=dtype)
