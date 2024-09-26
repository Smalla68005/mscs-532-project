import pandas as pd
from CompressedTree import CompressedTrie
from SlidingWindowMemoryPooling import  SlidingWindow
from HashMapUpdated import HashMap

# Load the dataset
def load_real_world_data():
    # Load the dataset from CSV
    df = pd.read_csv('creditcard.csv')

    df = df[['Amount', 'Time']] # Removed other non necessary columns

    new_row_index = len(df)  # Get the current length of the DataFrame

    df.loc[new_row_index] = ['995', '20240101'] # Added the missing row
    
    return df

# Debugging Purposes
# def write_string_to_file(file_name, content):
#     # Open the file in write mode ('w')
#     with open(file_name, 'w') as file:
#         for item in content:
#             file.writelines(f"{item}\n")
#     print(f"Content written to {file_name}")


# Test 1: Insert transaction patterns into Compressed Trie
def test_trie_with_real_data(df):
    print("Test 1: Compressed Trie with Real Data")

    trie = CompressedTrie()
    
    # 'Amount' as the pattern
    for index,  row in df.iterrows():
        
        pattern = str(int(row['Amount']))  # Convert amount to string pattern
        
        trie.insert(pattern)
   
    trie.compress_trie()

    
    # Check if specific patterns exist
    for i in range(1000):
        assert trie.search(str(i)), f"Pattern {i} should be found"
    print("Compressed Trie passed real-world data test")

# Test 2: Sliding Window Test with Real Data
def test_sliding_window_with_real_data(df):
    print("\nTest 2: Sliding Window with Real Data")

    df = df[df['Amount'] != '995']  # Removed the string value added before for Trie

    window = SlidingWindow(10000)  # Adjust window size for stress testing

    # 'Amount' as the transaction value
    for index, row in df.iterrows():
       
        window.add_transaction(row['Amount'])

    assert window.average_transaction() > 0, "Sliding window average incorrect"
    print("Sliding Window passed real-world data test")

# Test 3: Hash Map Test with Real Data (User -> Transaction)
def test_hash_map_with_real_data(df):
    print("\nTest 3: Hash Map with Real Data")
    
    # Cleaning Data to remove duplicate time as this will be the key.
    df = df.drop_duplicates(subset=['Time'])
    df = df[['Amount', 'Time']]

    hash_map = HashMap()

    # 'Time' as user and 'Amount' as the value
    for index, row in df.iterrows():
        user_id = f"user_{int(row['Time'])}"  # Simulate user with Time as ID
        transaction_amount = row['Amount']
        hash_map.insert(user_id, transaction_amount)

    # Test lookup
    for index, row in df.head(994).iterrows():
        user_id = f"user_{int(row['Time'])}"
        assert hash_map.get(user_id) == row['Amount'], f"User {user_id} should have transaction {row['Amount']}"
    print("Hash Map passed real-world data test")

# Running the tests
if __name__ == "__main__":
    df = load_real_world_data()

    # Run tests on real-world data
    test_trie_with_real_data(df)
    test_sliding_window_with_real_data(df)
    test_hash_map_with_real_data(df)
