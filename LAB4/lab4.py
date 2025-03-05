class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        
        last = self.head
        while last.next:  # Traverse until the last node
            last = last.next
        
        last.next = new_node  # Insert the new node at the end

    def delete_node(self, data):
        """Delete the first node with the specified data."""
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == data:
            self.head = current.next  # Move the head to the next node
            current = None  # Free the memory
            return
        
        prev = None
        # Search for the node to be deleted
        while current and current.data != data:
            prev = current
            current = current.next
        
        # If the node with the data wasn't found
        if current is None:
            return
        
        # Unlink the node from the list
        prev.next = current.next
        current = None  # Free the memory

    def traverse(self):
        """Traverse and print the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()  # For new line after the traversal

# Example usage:
linked_list = LinkedList()

# 1. Insert 10 at the beginning
linked_list.insert_at_beginning(10)
# 2. Insert 20 at the beginning
linked_list.insert_at_beginning(20)
# 3. Insert 30 at the beginning
linked_list.insert_at_beginning(30)

print("Linked list after inserting 30, 20, 10 at the beginning:")
linked_list.traverse()  # Output: 30 -> 20 -> 10

# 4. Insert 5 at the end
linked_list.insert_at_end(5)
# 5. Insert 10 at the end
linked_list.insert_at_end(10)
# 6. Insert 15 at the end
linked_list.insert_at_end(15)
# 7. Insert 20 at the end
linked_list.insert_at_end(20)

print("\nLinked list after inserting 5, 10, 15, 20 at the end:")
linked_list.traverse()  # Output: 30 -> 20 -> 10 -> 5 -> 10 -> 15 -> 20

# 8. Delete the node with data 20
linked_list.delete_node(20)

print("\nLinked list after deleting node with data 20:")
linked_list.traverse()  # Output: 30 -> 20 -> 10 -> 5 -> 10 -> 15

# 9. Traverse the list again
print("\nTraversing the linked list:")
linked_list.traverse()  # Output: 30 -> 20 -> 10 -> 5 -> 10 -> 15

