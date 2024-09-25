from Trie import Trie
from SlidingWindow import SlidingWindow
from UserTransactionHistory import UserTransactionHistory

# Test 1: Robustness for Trie with Error Handling
def test_trie():
    print("\nTest 1: Trie Pattern Matching with Error Handling")
    trie = Trie()
    
    try:
        trie.insert("")
    except ValueError as e:
        print(f"Error handled for empty pattern: {e}")
    
    try:
        trie.insert(123456)  # Invalid input, not a string
    except ValueError as e:
        print(f"Error handled for non-string input: {e}")
    
    trie.insert("123456")
    trie.insert("789101")

    print("Searching for pattern '123456':", "Found" if trie.search("123456") else "Not Found")
    print("Searching for pattern '654321':", "Found" if trie.search("654321") else "Not Found")
    
    try:
        trie.search(123456)  # Invalid search input
    except ValueError as e:
        print(f"Error handled for non-string search input: {e}")

# Test 2: Sliding Window with Error Handling
def test_sliding_window():
    print("\nTest 2: Sliding Window with Error Handling")
    try:
        window = SlidingWindow(-1)  # Invalid window size
    except ValueError as e:
        print(f"Error handled for invalid window size: {e}")
    
    window = SlidingWindow(3)

    try:
        window.add_transaction("invalid")  # Invalid transaction input
    except ValueError as e:
        print(f"Error handled for invalid transaction input: {e}")
    
    window.add_transaction(100)
    window.add_transaction(200)
    window.add_transaction(150)

    print("Average transaction in window:", window.average_transaction())
    
    window.add_transaction(300)
    print("Average transaction after adding a new one:", window.average_transaction())

# Test 3: Hash Map for User Transaction History with Error Handling
def test_user_transaction_history():
    print("\nTest 3: Hash Map for User Transaction History with Error Handling")
    history = UserTransactionHistory()
    
    try:
        history.add_transaction("", 100)  # Invalid user identifier
    except ValueError as e:
        print(f"Error handled for invalid user identifier: {e}")
    
    try:
        history.add_transaction("user1", "invalid")  # Invalid transaction
    except ValueError as e:
        print(f"Error handled for invalid transaction: {e}")
    
    history.add_transaction('user1', 100)
    history.add_transaction('user1', 200)
    
    print("Transaction history for user1:", history.get_history('user1'))
    
    try:
        print("Transaction history for invalid user:", history.get_history(123))
    except ValueError as e:
        print(f"Error handled for invalid user identifier: {e}")

# Running the tests
if __name__ == "__main__":
    test_trie()
    test_sliding_window()
    test_user_transaction_history()
