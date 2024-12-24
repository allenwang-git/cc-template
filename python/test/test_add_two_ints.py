from python.add_two_ints import add_two

def test_add_two():
    assert add_two(1, 3) == 4
    assert add_two(-1, 3) == 2
