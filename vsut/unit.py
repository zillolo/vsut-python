from collections import namedtuple
from enum import Enum
from math import floor, log10
from sys import stdout
from vsut.assertion import AssertException

AssertionFail = namedtuple("Fail", "id, exception")


class Unit():

    def __init__(self):
        self.tests = [(id, funcName) for id, funcName in enumerate([method for method in dir(self)
                                                                    if callable(getattr(self, method)) and method.startswith("test")])]
        self.failedAssertions = []

    def run(self):
        for id, test in self.tests:
            try:
                # Get the method that needs to be executed.
                func = getattr(self, test, None)

                # Run the setup method.
                self.setup()
                # Run the test method.
                func()
                # Run the teardown method.
                self.teardown()
            except AssertException as e:
                self.failedAssertions.append(AssertionFail(id, e))

    def setup(self):
        pass

    def teardown(self):
        pass


class Formatter():

    def __init__(self, unit, out=stdout):
        self.unit = unit
        self.output = out

    def print(self):
        pass


class TableFormatter(Formatter):

    def print(self):
        print("Case -> {0}".format(type(self.unit).__name__), file=self.output)

        idLength = int(floor(log10(len(self.unit.tests)))) + 3
        nameLength = max([len(test[1]) for test in self.unit.tests])

        if len(self.unit.failedAssertions) != 0:
            assertLength = max(
                [len(fail.exception.assertion.__name__) for fail in self.unit.failedAssertions]) + 2
        else:
            assertLength = 0

        for id, test in self.unit.tests:
            fails = [
                fail.exception for fail in self.unit.failedAssertions if fail.id == id]
            if len(fails) == 0:
                print("\t{0:>{idLength}} {1:<{nameLength}} -> Ok".format(
                    "[{0}]".format(id), test, idLength=idLength, nameLength=nameLength), file=self.output)
            else:
                for fail in fails:
                    message = fail.message
                    if message is not None and message != "":
                        message = "-> {0}".format(fail.message)
                    print("\t{0:>{idLength}} {1:<{nameLength}} -> Fail | {2:<{assertLength}} {3}".format("[{0}]".format(id), test, "[{0}]".format(
                        fail.assertion.__name__), message, idLength=idLength, nameLength=nameLength, assertLength=assertLength), file=self.output)
