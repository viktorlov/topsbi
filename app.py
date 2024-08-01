import pandas as pd

from FixedVariables.constants import Classes__dict, plm__dict, plmHierarchy__dict
from LoguruModule.code import LoguruDecoratorClass
from PostgresDBModule.code import PostgresDBClass


class ApplicationClass:

    @LoguruDecoratorClass(level="INFO")
    def load_data(self):

        db = PostgresDBClass()

        Classes = pd.read_csv('./CSVData/Classes.csv')
        db.load_dataframe(Classes, 'Classes', dtype=Classes__dict)

        plm = pd.read_csv('./CSVData/plm.csv')
        db.load_dataframe(plm, 'plm', dtype=plm__dict)

        plmHierarchy = pd.read_csv('./CSVData/plmHierarchy.csv')
        db.load_dataframe(plmHierarchy, 'plmHierarchy', dtype=plmHierarchy__dict)


if __name__ == "__main__":
    app = ApplicationClass()
    app.load_data()
