from abc import ABC, abstractstaticmethod
from creational.absratc_factory.chair_factory import ChairFactory
from creational.absratc_factory.table_factory import TableFactory


class IFurnitureFactory(ABC):

    @abstractstaticmethod
    def get_furniture(furniture_type):
        """The static furniture factory method"""


class FurnitureFactory(IFurnitureFactory):
    @staticmethod
    def get_furniture(furniture_type):
        try:
            if furniture_type in ["Chair1", "Chair2"]:
                return ChairFactory.get_chair(furniture_type)
            if furniture_type in ["Table1", "Table2"]:
                return TableFactory.get_table(furniture_type)
            raise AssertionError("Can not find furniture")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    furniture = FurnitureFactory.get_furniture("Chair1")
    print(furniture)

