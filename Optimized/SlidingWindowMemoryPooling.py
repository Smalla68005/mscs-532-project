from collections import deque

class SlidingWindow:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Window size must be a positive integer.")
        self.window = deque(maxlen=size)

        # Memory pool for better management
        self.transaction_pool = [None] * size  

    def add_transaction(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Transaction amount must be a valid number." )
        self.window.append(amount)

    def average_transaction(self):
        if not self.window:
            return 0
        return sum(self.window) / len(self.window)

    def pool_memory(self):
        """ Pool memory for optimized deque operations. """
        # Memory optimization can be applied for very large windows
        pass


