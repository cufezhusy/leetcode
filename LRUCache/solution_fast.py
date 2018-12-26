# ===================================================================================
# Use double linked node
# ===================================================================================

class Node:

    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.s = 0
        self.c = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        else:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            self.remove(self.map[key])
        elif self.s == self.c:
            p = self.head.k
            self.remove(self.map[p])
            self.map.pop(p)
        else:
            self.s += 1

        node = Node(key, value)
        self.map[key] = node
        self.add(node)

    def add(self, node):
        if self.head:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node
        else:
            self.head = self.tail = node

    def remove(self, node):
        if self.head and self.tail and self.head == self.tail:
            self.head = self.tail = None
        else:
            if self.head == node:
                self.head = node.next
                return
            if self.tail == node:
                self.tail = node.prev
                return
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.put(2,33)
print(obj.get(2))
print(obj.get(1))