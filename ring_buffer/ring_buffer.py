from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == 0:  # don't append if capacity = zero
            return

        if len(self.storage) == self.capacity:
            if not self.current:
                self.current = self.storage.tail  # replace when capacity is full

            self.current.value = item
            self.current = self.current.prev
        else:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if len(self.storage) == 0:
            return list_buffer_contents  # return empty list if storage is empty

        current = self.storage.tail
        list_buffer_contents.append(current.value)

        while current.prev:
            current = current.prev
            list_buffer_contents.append(current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
