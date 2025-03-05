class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    def append_node(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True 
            current = current.next
        return False  
    
    def display_list(self):
        """Print the linked list."""
        current = self.head
        if not current:
            print("The list is empty.")
            return
        
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print() 

# Example usage
linked_list = SinglyLinkedList()

# Append nodes to the list
linked_list.append_node(90)
linked_list.append_node(70)
linked_list.append_node(30)

# Display the list
print("Linked list after appending nodes:")
linked_list.display_list()  

# Search for nodes
print("\nNode with data 90:", linked_list.search_node(90))  
print("Node with data 70:", linked_list.search_node(70))  
