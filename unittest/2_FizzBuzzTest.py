# cf. https://www.linkedin.com/learning/unit-testing-and-test-driven-development-in-python/example-tdd-session-the-fizzbuzz-kata?u=26192810

import pytest


def fizzBuzz(x):
    return str(x)


def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal


def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")
