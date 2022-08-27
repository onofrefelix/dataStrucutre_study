from double_linkedlist.dlinked_list import DoubleLinkedlist


class TestClass:
    dlinklist = DoubleLinkedlist()

    # value = 10
    # dlinklist.push(value)
    # dlinklist.push(value + 1)
    # dlinklist.push(value + 2)
    # dlinklist.push(value + 3)

    def test_get_head(self):
        assert self.dlinklist.get_head().get_next_pointer() is not None
        assert self.dlinklist.get_head().get_previous_pointer() is None

    def test_get_tail(self):
        assert self.dlinklist.get_tail().get_next_pointer() is None
        assert self.dlinklist.get_tail().get_previous_pointer() is not None

    def test_insert_head(self):
        val = 9
        for i in range(10):
            self.dlinklist.push(i)
        val_calc = self.dlinklist.get_head().get_next_pointer().get_item()

        assert val_calc == val

    def test_append(self):
        val = 9
        for i in range(10):
            self.dlinklist.append(i)

        assert self.dlinklist.get_tail().get_previous_pointer().get_item() == val

    def test_delete(self):

        addr_head_next = self.dlinklist.get_head().get_next_pointer()
        addr_tail_prev = self.dlinklist.get_tail().get_next_pointer()

        for i in range(10):
            self.dlinklist.append(i)
        for j in range(5):
            self.dlinklist.delete_item(j)

        assert self.dlinklist.get_head().get_next_pointer().get_item() == 5

    def test_insert_item_at_position(self):

        self.dlinklist.push(100)
        val = self.dlinklist.insert_item_at_position(1, 222)
        val_experado = True
        assert val == val_experado
