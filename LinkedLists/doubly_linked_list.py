class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def set_new_next(self, next=None):
        self.next = next

    def set_new_previous(self, previous=None):
        self.previous = previous

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, data=None):
        node = Node(data=data)
        node.set_new_next(self.head)
        self.head.set_new_previous(node)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        current = self.head
        print("this is the list")
        print("----------------")
        while current:
            print(current.get_data())
            current = current.get_next()
        print("----------------")
        print("end of the list")

    def search_first_index(self, data_to_find=None):
        current = self.head
        while current:
            #print(current.get_data())
            if current.get_data() == data_to_find:
                return current
            current = current.get_next()
        return None
        # raise ValueError("data is not in list!")

    def delete_one(self, data_to_delete=None):
        current = self.head
        while current.get_next():
            if current.get_next().data == data_to_delete:
                node_to_return = current.get_next()
                try:
                    current.get_next().get_next().set_new_previous(current)
                except AttributeError:
                    pass
                current.set_new_next(current.get_next().get_next())
                return node_to_return
            current = current.get_next()
        
if __name__ == "__main__":
    head = Node(data="ayy")
    singly_linked_list = DoublyLinkedList(head)
    singly_linked_list.insert_at_head("bee")
    singly_linked_list.insert_at_head("cee")
    print(singly_linked_list.size())
    print(singly_linked_list.search_first_index("bee")) # should print an instance of a node
    print(singly_linked_list.search_first_index("zee"))
    print(singly_linked_list.delete_one("cee"))
    singly_linked_list.print_list()
