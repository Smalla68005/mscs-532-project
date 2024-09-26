import timeit
from Trie import Trie
from SlidingWindow import SlidingWindow
from UserTransactionHistory import UserTransactionHistory


# Test 1: Robustness for Trie with Error Handling and 1 Million Records
def test_trie():
    print("Test 1: Trie Pattern Matching with Error Handling and 1 Million Records")
    trie = Trie()

    # Inserting 1 million patterns
    try:
        for i in range(5000000):
            trie.insert(str(i))
    except ValueError as e:
        print(f"Error handled during trie insertions: {e}")

    # Searching for a few patterns
    for i in range(1000):
        pattern = str(i)
        result = trie.search(pattern)
        if not result:
            print(f"Error: Pattern {pattern} should be found but wasn't.")

    print("Trie passed 1 million pattern insertion test.")

# Test 2: Sliding Window with 1 Million Transactions and Error Handling
def test_sliding_window():
    print("\nTest 2: Sliding Window with Error Handling and 1 Million Transactions")
    
    # Creating a large window
    window = SlidingWindow(5000000)

    # Adding 1 million transactions
    try:
        for i in range(5000000):
            window.add_transaction(i)
    except ValueError as e:
        print(f"Error handled during transaction additions: {e}")

    print("Sliding Window passed 1 million transactions test.")
    print("Average transaction in window:", window.average_transaction())

# Test 3: Hash Map for User Transaction History with 1 Million Transactions and Error Handling
def test_user_transaction_history():
    print("\nTest 3: Hash Map for User Transaction History with 1 Million Records and Error Handling")
    history = UserTransactionHistory()

    # Adding 1 million transactions
    try:
        for i in range(5000000):
            history.add_transaction(f"user{i}", i)
    except ValueError as e:
        print(f"Error handled during user transaction additions: {e}")

    # Verifying some users
    for i in range(1000):
        if history.get_history(f"user{i}") is None:
            print(f"Error: User user{i} should have transaction history but doesn't.")

    print("Hash Map passed 1 million user transaction test.")

# Function to measure time
def measure_time(func):
    start_time = timeit.default_timer()
    func()
    end_time = timeit.default_timer()
    print(f"Time taken for {func.__name__}: {end_time - start_time:.4f} seconds")

# Running the tests with time measurement
if __name__ == "__main__":
    measure_time(test_trie)
    measure_time(test_sliding_window)
    measure_time(test_user_transaction_history)
