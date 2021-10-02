class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next =  None


class LRUCache:

    def __init__(self, capacity):
        self.has = {}
        self.cap = capacity
        self.root = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.root
        self.root.next = self.tail
        
    def get(self, key):
        if key in self.has:
            val = self.has[key].data
            self.remove(self.has[key])
            self.has[key] = Node(key, val)
            self.add(self.has[key])
            return val
        return -1
    
    def put(self, key, value):
        if key in self.has:
            self.remove(self.has[key])
            self.has[key] = Node(key, value)
            self.add(self.has[key])
        else:
            self.has[key] = Node(key, value)
            self.add(self.has[key])
        if len(self.has) == self.cap+1:
            self.has.pop(self.root.next.key)
            self.remove(self.root.next)
            
    def add(self, node):
        c = self.tail.prev
        c.next = node
        node.prev = c
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        