from hello import hello

def test_hello_default():
    assert hello()=="Hello, world"

def test_hello():
    assert hello("David")=="Hello, David"
    