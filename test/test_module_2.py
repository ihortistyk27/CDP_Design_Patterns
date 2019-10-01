from test.logger import Logger

logger = Logger("C:\\CDP_Design_Patterns\\test\\test.log")


class TestModule2:
    @staticmethod
    def function_m2():
        logger.critical("CRITICAL", "INSIDE MODULE @2")
        print("def function_m2")
