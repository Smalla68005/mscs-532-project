from Trie import Trie
from SlidingWindow import SlidingWindow
from UserTransactionHistory import UserTransactionHistory

# Test 1: Demonstrating Trie for Fraud Pattern Matching
def test_trie():
    print("Test 1: Trie Pattern Matching")
    trie = Trie()
    
    # Insert fraud patterns
    trie.insert("123456")
    trie.insert("789101")
    trie.insert("356Dba")

    # Test search for existing pattern
    print("Searching for pattern '123456':", "Found" if trie.search("123456") else "Not Found")
    
    # Test search for non-existent pattern
    print("Searching for pattern '654321':", "Found" if trie.search("654321") else "Not Found")

# Test 2: Sliding Window for Recent Transactions
def test_sliding_window():
    print("\nTest 2: Sliding Window for Recent Transactions")
    window = SlidingWindow(3)  # Window size of 3
    
    # Add transactions
    window.add_transaction(100)
    window.add_transaction(200)
    window.add_transaction(150)
    
    # Check average of current window
    print("Average transaction in window:", window.average_transaction())
    
    # Add a new transaction and check average
    window.add_transaction(300)
    print("Average transaction after adding a new one:", round(window.average_transaction(),3))

# Test 3: Hash Map for User Transaction History
def test_user_transaction_history():
    print("\nTest 3: Hash Map for User Transaction History")
    history = UserTransactionHistory()
    
    # Add transactions for user 'user1'
    history.add_transaction('user1', 100)
    history.add_transaction('user1', 200)
    history.add_transaction('user1', 300)
    
    # Retrieve history for user 'user1'
    print("Transaction history for user1:", history.get_history('user1'))
    
    # Check for a user with no history
    print("Transaction history for user2 (no transactions):", history.get_history('user2'))

# Running the tests
if __name__ == "__main__":
    test_trie()
    test_sliding_window()
    test_user_transaction_history()