import pytest
from arrays import Array


def test_array():
    arr = Array(1)
    assert isinstance(arr, Array)


def test_len_met():
    arr = Array(1)
    assert len(arr) == 1


def test_str_met():
    arr = Array(1)
    assert str(arr) == '[None]'


def test_iter_met():
    arr = Array(3, 1)
    val = 0
    val_esperado = 1
    for i in arr:
        val = i
    assert val == val_esperado


def test_getitem():
    arr = Array(3, 1)
    val = arr[0]
    val_esperado = 1
    assert val == val_esperado


def test_append_new_item():
    arr = Array(0)
    val = arr[0]
    val_esperado = 1
    assert val == val_esperado


def test_getitem_out_of_range():
    try:
        index = 5
        arr = Array(3, 1)
        val = arr[index]
        val_esperado = 1
    except ValueError as err:
        assert str(err) == f'index -> {index} out of range'


def test_setitem_out_of_range():
    try:
        index = 5
        arr = Array(3, 1)
        arr[index] = 1
        val_esperado = 1
    except ValueError as err:
        assert str(err) == f'index -> {index} out of range'


def test_setitem():
    arr = Array(3, 1)
    val = 2
    arr[0] = val
    val_esperado = 2
    assert val == val_esperado
    arr[2] = val
    assert arr[2] == val_esperado
