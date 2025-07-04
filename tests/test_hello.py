from template_pkg.hello import hello


def test_hello():
    assert hello() == "Hello, World!"
