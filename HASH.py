class HASH:
    def __init__(self):
        self.hash_table = list(None)*20 
    def hash(self,value):
        hash_index = hash(value) % 20
        return hash_index
    def insert(self,value):
        hash_index = self.hash(values)
        while self.hash_table[hash_index] is not None:
            hash_index = (hash_index+1)%20
        self.hash_table[hash_index] = value
    def search(self,value):
        hash_index = self.hash(value)
        while self.hash_table[hash_index] != value:
            hash_index = (hash_index+1)%20
            if self.hash_table[hash_index] is None:
                print("So such element found")
                return
        if self.hash_table[hash_index] == value:
            print("Element found at index",hash_index)
    def delete(self,value):
        hash_index = self.hash(value)
        while self.hash_table[hash_index] != value:
            hash_index = (hash_index+1)%20
            if self.hash_table[hash_index] is None:
                print("So such element found")
                return
        if self.hash_table[hash_index] == value:
            self.hash_table[hash_index] = None
            print("Element deleted")

        

