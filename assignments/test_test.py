from test import function_hello
import pytest

def test_function_hello():
    assert x == "hello world"


pytest.main(["-v", "--tb=line", "-rN", __file__])