# Fractional Knapsack Problem using the Greedy Algorithm.

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value of items in the knapsack
def fractional_knapsack(capacity, items):
    # Calculate value-to-weight ratio for each item
    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    
    total_value = 0.0  # Total value accumulated in the knapsack
    for item in items:
        if capacity == 0:  # If the knapsack is full, break
            break
        # If item can be fully added to the knapsack
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
            print(f"Taking full item with value {item.value} and weight {item.weight}")
        else:
            # Take fraction of the remaining capacity
            fraction = capacity / item.weight
            total_value += item.value * fraction
            print(f"Taking {fraction * 100:.2f}% of item with value {item.value} and weight {item.weight}")
            capacity = 0  # Knapsack is now full

    return total_value

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []
    for i in range(n):
        value = float(input(f"Enter value of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the maximum weight capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)
    print(f"\nMaximum value in the knapsack: {max_value}")
