import sorts

def test_partition_base():
    list = [11,2,4,57,7,89,7,654,3,22,1]
    expected = [2,4,7,7,3,1], [11],[57,89,654,22]
    actual = sorts.partition(list)
    assert actual==expected


def test_partition_nothing_less():
    list = [1,2,4,57,7,89,7,654,3,11,22]
    expected = [],[1],[2,4,57,7,89,7,654,3,11,22]
    actual = sorts.partition(list)
    assert actual==expected

def test_partition_nothing_more():
    list = [660,2,4,57,7,89,7,654,3,11,22,1]
    expected = [2,4,57,7,89,7,654,3,11,22,1],[660],[]
    actual = sorts.partition(list)
    assert actual==expected