class HashTable:
    def __init__(self):
        self.maxSize = 100
        self.storageArray = [[] for i in range(self.maxSize)]

    def getHash(self, key):
        hashSum = 0
        for keyChar in key:
            hashSum += ord(keyChar)
        return hashSum % self.maxSize

    def __setitem__(self, key, value):
        hash = self.getHash(key)
        for id, keyValPair in enumerate(self.storageArray[hash]):
            if keyValPair[0] == key:
                self.storageArray[hash][id][1] = value
                return
        self.storageArray[hash].append([key, value])

    def __getitem__(self, key):
        hash = self.getHash(key)
        values = self.storageArray[hash]
        if values == []:
            return None
        for keyVarPair in values:
            if keyVarPair[0] == key:
                return keyVarPair[1]
        return None

    def __delitem__(self, key):
        hash = self.getHash(key)
        values = self.storageArray[hash]
        for id, keyValPair in enumerate(values):
            if keyValPair[0] == key:
                values.pop(id)


if __name__ == "__main__":
    ht = HashTable()
    ht["marchad"] = "Roshan"
    ht["marchbc"] = "Dash"
    del ht["marchbc"]
    print(f"My name is {ht['marchad']} {ht['marchbc']}!")
