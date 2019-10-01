from abc import ABC, abstractstaticmethod


class IChair(ABC):
    @abstractstaticmethod
    def get_dimension():
        """The Chair Interface"""


class Chair1(IChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimension(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class Chair2(IChair):
    def __init__(self):
        self.height = 60
        self.width = 60
        self.depth = 40

    def get_dimension(self):
        return {"height": self.height, "width": self.width, "depth": self.depth}


class ChairFactory(object):
    @staticmethod
    def get_chair(chairtype):
        try:
            if chairtype == "Chair1":
                print(chairtype, " <<< chair type")
                return Chair1()
            if chairtype == "Chair2":
                print(chairtype, " <<< chair type")
                return Chair2()
            raise AssertionError("Chair not found!")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    chair1 = ChairFactory.get_chair("Chair1")
    print(chair1.get_dimension())
    chair2 = ChairFactory.get_chair("Chair2")
    print(chair2.get_dimension())
