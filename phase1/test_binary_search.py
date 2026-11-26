from binary_search import binarySearch

A = [1, 5, 6, 9, 15, 22]


def test_found():
    assert binarySearch(A, 9) == 3


def test_not_found():
    assert binarySearch(A, 4) == -1


def test_first_index():
    assert binarySearch(A, 1) == 0


def test_last_index():
    assert binarySearch(A, 22) == 5