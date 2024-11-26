""" Implement the stack by using a linked list and display its values.Perform all the operations related to the stack."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push a value onto the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack.")

    # Pop a value from the stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped {popped_node.data} from the stack.")
        return popped_node.data

    # Peek at the top value of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top element is {self.top.data}.")
        return self.top.data

    # Display all elements in the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Stack elements are:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Main program with user menu
def main():
    stack = Stack()
    
    while True:
        print("\nSelect an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check if Empty")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            data = int(input("Enter the value to push: "))
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
