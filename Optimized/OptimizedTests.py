import timeit
from CompressedTree import CompressedTrie
from SlidingWindowMemoryPooling import SlidingWindow
from HashMapUpdated import HashMap

# Test 1: Compressed Trie Stress Test
def test_trie():
    print("Test 1: Compressed Trie")
    trie = CompressedTrie()

    # Insert many patterns
    for i in range(1000000):
        pattern = str(i)
        trie.insert(pattern)

    trie.compress_trie()

    # Perform search after compression
    for i in range(1000):
        assert trie.search(str(i)), f"Pattern {i} should be found"
    print("Compressed Trie passed 1 million patterns stress test")

# Test 2: Sliding Window Stress Test
def test_sliding_window():
    print("\nTest 2: Sliding Window")
    window = SlidingWindow(1000000)  # Large window size

    # Add a large number of transactions
    for i in range(1000000):
        window.add_transaction(i)

    assert window.average_transaction() == sum(range(1000000)) / 1000000, "Sliding window average incorrect"
    print("Sliding Window passed 1 million transactions stress test")

# Test 3: Hash Map Stress Test
def test_hash_map():
    print("\nTest 3: Hash Map")
    hash_map = HashMap()

    # Insert many users
    for i in range(1000000):
        hash_map.insert(f"user{i}", i)

    # Test lookup
    for i in range(1000):
        assert hash_map.get(f"user{i}") == i, f"User {i} should be found"
    print("Hash Map passed 1 million users stress test")


# Function to measure time
def measure_time(func):
    start_time = timeit.default_timer()
    func()
    end_time = timeit.default_timer()
    print(f"Time taken for {func.__name__}: {end_time - start_time:.4f} seconds")

# Running the tests
if __name__ == "__main__":
    print("\nTesting the Optimized Data Structures")
    measure_time(test_trie)
    measure_time(test_sliding_window)
    measure_time(test_hash_map)
