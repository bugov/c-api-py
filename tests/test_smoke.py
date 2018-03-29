import secure_string


def test_smoke():
    s = 'secret'
    secure_string.flush(s)
    assert s == '\x00' * len(s)
