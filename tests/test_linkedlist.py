from slinkedlist.linkedlist import LinkedList
from nodes.node import Node


def test_linked_list_instance():
    lkl = LinkedList()

    assert isinstance(lkl, LinkedList)


def test_linked_list_append():
    index_val = 0
    val = 10
    lkl = LinkedList()
    lkl.append(val)
    valor_esperado = lkl[index_val]

    assert val == valor_esperado


def test_linked_list_qtd_elem_List():
    index_val = 8888
    valor_esperado = 1
    lkl = LinkedList()
    lkl.append(index_val)
    val = len(lkl)

    assert val == valor_esperado


def test_linked_list_getitem_index_out_of_range():
    index_val = 1
    valor_esperado = f"Index -> {index_val} Out of Range"
    try:
        val = 10
        lkl = LinkedList()
        val = lkl[index_val]
    except IndexError as err:
        val = str(err)

    assert val == valor_esperado


def test_linked_list_setitem():
    index_val = 0
    val = 10
    lkl = LinkedList()
    lkl.append(val + 1)
    lkl[0] = val
    valor_esperado = lkl[index_val]

    assert val == valor_esperado


def test_linked_list_setitem_index_out_of_range():
    index_val = 100
    valor_esperado = f"Index -> {index_val} Out of Range"
    try:
        val = 10
        lkl = LinkedList()
        lkl.append(val)
        lkl[index_val] = val + 1

    except IndexError as err:
        val = str(err)

    assert val == valor_esperado


def test_linked_list_insert():
    index_val0 = 0
    val0 = 0
    lkl = LinkedList()
    lkl.append(0)
    lkl.append(1)
    lkl.append(2)
    valor_esperado0 = lkl[index_val0]

    assert val0 == valor_esperado0
    assert val0 + 1 == lkl[1]
