class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.hash_table[index] is not None:
            index = (index + 1) % self.size
        self.hash_table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.hash_table[index] is not None and self.hash_table[index][0] != key:
            index = (index + 1) % self.size
        if self.hash_table[index] is None:
            return None
        else:
            return self.hash_table[index][1]


# Contoh penggunaan
hash_table = HashTable(10)
hash_table.insert(10, 'a')
hash_table.insert(20, 'b')
hash_table.insert(30, 'c')

print("Hasil pencarian untuk kunci 10:", hash_table.search(10))
print("Hasil pencarian untuk kunci 20:", hash_table.search(20))
print("Hasil pencarian untuk kunci 30:", hash_table.search(30))
print("Hasil pencarian untuk kunci 40:", hash_table.search(40))