class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            # Insert new node at beginning
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def delete_node(self, data):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        prev = None

        while True:
            if current.data == data:
                if current == self.head:
                    # only one node
                    if current.next == self.head:
                        self.head = None
                    else:
                        # More than one node
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = current.next
                return  # Node deleted

            prev = current
            current = current.next

            if current == self.head:
                break  # back to head

        print(f"Node with data {data} not found.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        nodes = []
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(nodes))

# Example usage:
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)

cll.display()  
cll.delete_node(20)
cll.display()  



