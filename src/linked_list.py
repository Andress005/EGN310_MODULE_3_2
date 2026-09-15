class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        new_node.next = current.next
        current.next = new_node

    def remove(self, data):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

        raise ValueError("Data not found")

    def find(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None

    def to_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values

    def __len__(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def is_empty(self):
        return self.head is None