from abc import ABC, abstractstaticmethod


class ITable(ABC):
    @abstractstaticmethod
    def get_dimension():
        """The Chair Interface"""


class Table1(ITable):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimension(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class Table2(ITable):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 40

    def get_dimension(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class TableFactory(object):
    @staticmethod
    def get_table(table_type):
        try:
            if table_type == "Table1":
                print(table_type, " <<< table type")
                return Table1()
            if table_type == "Table2":
                print(table_type, " <<< table type")
                return Table2()
            raise AssertionError("Table not found!")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    chair1 = TableFactory.get_table("Table1")
    print(chair1.get_dimension())
    chair2 = TableFactory.get_table("Table2")
    print(chair2.get_dimension())