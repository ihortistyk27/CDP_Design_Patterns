
from abc import ABCMeta, abstractstaticmethod


class ISubscriber(metaclass=ABCMeta):
    @abstractstaticmethod
    def update(message):
        """Get update"""


class SubscriberOne(ISubscriber):

    def __init__(self, name):
        self._name = name

    def update(self, message):
        if "dinner" in message:
            print("{} got message '{}'".format(self._name, message))


class SubscriberTwo(ISubscriber):

    def __init__(self, name):
        self._name = name

    def update(self, message):
        if "lunch" in message:
            print("{} got message '{}'".format(self._name, message))


class IPublisher(metaclass=ABCMeta):

    @abstractstaticmethod
    def register(self, subscriber):
        """Register an subscriber"""
    @abstractstaticmethod
    def unregister(self, subscriber):
        """Unregister an subscriber"""

    @abstractstaticmethod
    def dispatch(self, message):
        """Send a message!!!"""


class Publisher1(IPublisher):
    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        self.subscribers.append(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == "__main__":
    publisher = Publisher1()

    jon = SubscriberOne("Jon")
    peter = SubscriberTwo("Peter")
    ali = SubscriberTwo("Ali")

    publisher.register(jon)
    publisher.register(peter)
    publisher.register(ali)

    publisher.dispatch("it's lunch time!")

    publisher.unregister(peter)

    publisher.dispatch("it's dinner time!")
