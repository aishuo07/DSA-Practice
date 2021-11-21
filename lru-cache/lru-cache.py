class Node:
    
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash = {}
        self.cap = capacity

    def get(self, key):
        if key in self.hash:
            value = self.hash[key].data
            self.remove(key)  
            self.add(key, value)
            return self.hash[key].data
        return -1
        
    def put(self, key, value):
        if key in self.hash:
            self.remove(key)
            self.add(key, value)
        elif len(self.hash)<self.cap:
            self.add(key,  value)
        else:
            self.remove(self.head.next.key)
            self.add(key, value)
        
    def remove(self, key):
        self.hash[key].prev.next = self.hash[key].next
        self.hash[key].next.prev = self.hash[key].prev
        self.hash.pop(key)
    
    def add(self, key, value):
        self.hash[key] = Node(value, key)
        temp = self.tail.prev
        self.hash[key].prev = temp
        self.hash[key].next = self.tail
        self.tail.prev = self.hash[key]
        temp.next = self.hash[key]
        