class HashMap:
    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.capacity = initial_capacity
        self.size = 0
        self.load_factor = load_factor
        self.map = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        """ Resize the hash map when load factor is exceeded. """
        old_map = self.map
        self.capacity *= 2
        self.map = [None] * self.capacity
        self.size = 0
        for entry in old_map:
            if entry:
                self.insert(entry[0], entry[1])

    def insert(self, key, value):
        if self.size / self.capacity > self.load_factor:
            self._resize()

        index = self._hash(key)
        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = (key, value)
                return
            
            # Open addressing with linear probing
            index = (index + 1) % self.capacity 

        self.map[index] = (key, value)
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        while self.map[index] is not None:
            if self.map[index][0] == key:
                return self.map[index][1]
            index = (index + 1) % self.capacity
        return None

# Example usage
hash_map = HashMap()
# hash_map.insert("user1", 100)
# hash_map.insert("user2", 200)
# hash_map.insert("user3", 300)

