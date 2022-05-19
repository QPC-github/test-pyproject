from pyproject.main import Foo


def test_foo():
    foo = Foo()
    assert foo.bar == "foofoo"
