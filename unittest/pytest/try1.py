import pytest


@pytest.fixture()
def hello():
    return "hello"


def test_string(hello):
    assert hello == "hello", "fixture should return hello"


if __name__ == '__main__':
    test_string(hello)
