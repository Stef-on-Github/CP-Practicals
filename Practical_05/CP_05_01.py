class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index (Indexing starts from 0)
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
            return
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from linked list by data
    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        while current_node and current_node.next and current_node.next.data != data:
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next

    # Print method for the linked list
    def printLL(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Create a new linked list
llist = LinkedList()

# Function to handle user input and operations
def menu():
    while True:
        # Display the menu options
        print("\nLinked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at Index")
        print("3. Insert at End")
        print("4. Remove First Node")
        print("5. Remove Last Node")
        print("6. Remove Node at Index")
        print("7. Remove Node by Data")
        print("8. Print Linked List")
        print("9. Exit")

        # Display the current state of the linked list before taking action
        print("\nCurrent Linked List:")
        llist.printLL()

        # Get user choice
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            data = input("Enter the data to insert at beginning: ").strip()
            llist.insertAtBegin(data)
        
        elif choice == '2':
            data = input("Enter the data to insert at index: ").strip()
            index = int(input("Enter the index: ").strip())
            llist.insertAtIndex(data, index)
        
        elif choice == '3':
            data = input("Enter the data to insert at end: ").strip()
            llist.insertAtEnd(data)
        
        elif choice == '4':
            llist.remove_first_node()
        
        elif choice == '5':
            llist.remove_last_node()
        
        elif choice == '6':
            index = int(input("Enter the index to remove: ").strip())
            llist.remove_at_index(index)
        
        elif choice == '7':
            data = input("Enter the data to remove: ").strip()
            llist.remove_node(data)
        
        elif choice == '8':
            print("Current Linked List:")
            llist.printLL()
        
        elif choice == '9':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

# Run the menu function to interact with the user
menu()
