
from abc import ABCMeta


class IUser(metaclass=ABCMeta):
    """A class whose instances want to interact with each other."""

    def send_message(self, message):
        """Send message"""


class User(IUser):
    """A class whose instances want to interact with each other."""

    def __init__(self, name):
        self.name = name
        self.chatRoom = ChatRoom()

    def send_message(self, message):
        self.chatRoom.display_message(self, message)

    def __str__(self):
        return self.name


class ChatRoom:
    """Mediator class."""

    def display_message(self, user, message):
        print("[{} says]: {}".format(user, message))


molly = User('Molly')
mark = User('Mark')
ethan = User('Ethan')

molly.send_message("Hi Team! Meeting at 3 PM today.")
mark.send_message("Roger that!")
ethan.send_message("Alright.")
