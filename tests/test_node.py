from nodes.node import Node


def test_node_instance():
    v1: int = 1
    node = Node(v1)
    assert isinstance(node, Node)


def test_getvalue_from_node():
    v1: int = 1
    node = Node(v1)
    val = node.getItem()
    val_esperado = 1

    assert val == val_esperado


def test_setvalue_from_node():
    v1 = 1
    node = Node(v1)
    node.setItem(v1)
    val = node.getItem()
    val_esperado = 1

    assert val == val_esperado


def test_get_next_pointer():
    v1: int = 1
    node = Node(v1)
    val = node.get_next_pointer()
    val_esperado = None

    assert val == val_esperado


def test_set_next_pointer():
    v1: int = 1
    node = Node(v1)
    node.set_next_pointer(node)
    val = node.get_next_pointer()
    val_esperado = node

    assert val == val_esperado
