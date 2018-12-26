class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keys = []
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys = [key] + self.keys
            return self.map[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.keys:
            self.keys = [key] + self.keys
        else:
            self.keys.remove(key)
            self.keys = [key] + self.keys

        self.map[key] = value
        if len(self.keys) > self.capacity:
            remove_key = self.keys[-1]
            self.keys = self.keys[:-1]
            self.map.pop(remove_key)

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.put(2,33)
print(obj.get(2))
obj.put(3,3)
print(obj.get(1))