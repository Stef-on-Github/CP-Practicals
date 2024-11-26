"""Implement a Circular Queue by using an array. Perform all the operations related to the circular queue."""

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Enqueue an element into the queue
    def enqueue(self, data):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue because the queue is full.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Enqueued {data} to the queue.")

    # Dequeue an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue because the queue is empty.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:  # Only one element in the queue
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Dequeued {data} from the queue.")
        return data

    # Peek at the front element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to peek.")
            return None
        print(f"Front element is {self.queue[self.front]}.")
        return self.queue[self.front]

    # Display all elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements are:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage of the CircularQueue class
if __name__ == "__main__":
    size = int(input("Enter the size of the circular queue: "))
    queue = CircularQueue(size)
    
    # Perform queue operations
    while True:
        print("\nSelect an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Check if Empty")
        print("6. Check if Full")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            data = int(input("Enter the value to enqueue: "))
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == '6':
            if queue.is_full():
                print("Queue is full.")
            else:
                print("Queue is not full.")
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
