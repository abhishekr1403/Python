class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return

        current_node = self.head
        llstr = ''
        while current_node:
            llstr += str(current_node.data) + '-->'
            current_node = current_node.next
        print(llstr)

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None  # What is the use of this?
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index!!!")

        if index == 0:
            self.head = self.head.next
            return

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index - 1:
                current_node.next = current_node.next.next
                break

            current_node = current_node.next
            current_index += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index!!!")

        if index == 0:
            self.insert_at_begining(data)

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break

            current_node = current_node.next
            current_index += 1

    # -------------Experimental_________________

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                current_node.next = Node(data_to_insert, current_node.next)
                break

            current_node = current_node.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        checker = 0
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                checker = 1
                break
            elif current_node.next.data != data:
                checker = checker
            current_node = current_node.next

        if not checker:
            print('The value is not in the linked list!')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()
