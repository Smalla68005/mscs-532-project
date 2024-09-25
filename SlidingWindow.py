from collections import deque

class SlidingWindow:
   
    def __init__(self, size):
        # Initialize a deque (double-ended queue) with a maximum length of 'size' to store recent transactions.
        if size <= 0:
            raise ValueError("Window size must be a positive integer.")
        self.window = deque(maxlen=size)

    # Method to add a new transaction (amount) to the sliding window.
    def add_transaction(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Transaction amount must be a valid number.")
        # Append the new transaction to the deque.
        # If the deque is full, the oldest transaction will be removed automatically.
        self.window.append(amount)

    # Method to calculate the average transaction amount from the values in the sliding window.
    def average_transaction(self):
        if not self.window:
            return 0
        # Return the average of the values in the window. 
        # If the window is empty, return 0 to avoid division by zero.
        return sum(self.window) / len(self.window) if self.window else 0
