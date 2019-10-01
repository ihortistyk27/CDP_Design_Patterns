from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    """The IBuilder Interface"""

    @abstractmethod
    def set_wall_material(self, value):
        """Set the wall material"""

    @abstractmethod
    def set_building_type(self, value):
        """Set the building type"""

    @abstractmethod
    def set_number_doors(self, value):
        """Set the building type"""

    @abstractmethod
    def set_number_windows(self, value):
        """Set the number of windows"""

    @abstractmethod
    def get_result(self):
        """Return the house"""


class HouseBuilder(IHouseBuilder):

    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        self.house.doors = value
        return self

    def set_number_windows(self, value):
        self.house.windows = value
        return self

    def get_result(self):
        return self.house


class House:
    """The Product"""

    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_material="brick"):
        # brick, wood, straw, ice
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hut, Castle, Duplex, Igloo, HouseBoat
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return "This is a {} {} with {} door(s) and {} window(s).".format(self.wall_material,
                                                                          self.building_type,
                                                                          self.doors,
                                                                          self.windows)


class IglooDirector:
    """The Director, building a different representation"""

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("Igloo") \
            .set_wall_material("Ice") \
            .set_number_doors(1) \
            .set_number_windows(4) \
            .get_result()


class HouseBoatDirector:
    """The Director, building a different representation"""

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("HouseBoat") \
            .set_wall_material("Wooden") \
            .set_number_doors(6) \
            .set_number_windows(8) \
            .get_result()


class CastleDirector:
    """The Director, building a different representation"""

    @staticmethod
    def construct():
        return HouseBuilder() \
            .set_building_type("Castle") \
            .set_wall_material("Granite") \
            .set_number_doors(12) \
            .set_number_windows(21) \
            .get_result()


if __name__ == "__main__":
    igloo = IglooDirector.construct()
    print(igloo)
    boat_house = HouseBoatDirector.construct()
    print(boat_house)
    castle = CastleDirector.construct()
    print(castle)
