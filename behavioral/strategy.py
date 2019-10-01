from abc import ABCMeta, abstractstaticmethod


class IStrategy(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute_algorithm(self):
        """Method to implement"""


class StrategyA(IStrategy):
    def __init__(self):
        IStrategy.__init__(self)

    def execute_algorithm(self):
        print("Concrete Strategy A")


class StrategyB(IStrategy):
    def __init__(self):
        IStrategy.__init__(self)

    def execute_algorithm(self):
        print("Concrete Strategy B")


class StrategyC(IStrategy):
    def __init__(self):
        IStrategy.__init__(self)

    def execute_algorithm(self):
        print("Concrete Strategy C")


#
# Context
# maintains a reference to a Strategy object
#
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.execute_algorithm()


if __name__ == "__main__":
    strategy_a = StrategyA()
    strategy_b = StrategyB()
    strategy_c = StrategyC()

    context = Context(strategy_a)
    context.context_interface()

    context = Context(strategy_b)
    context.context_interface()

    context = Context(strategy_c)
    context.context_interface()
