from test.logger import Logger

logger = Logger("C:\\CDP_Design_Patterns\\test\\test.log")


class TestModule1:

    @staticmethod
    def function_m1():
        logger.info("Info", "Inside MODULE @1")
        print("def function_m1")


