# Created ListNode to represent each node in a double-sided linked list 
# Also created this class to be able to initiate a node 
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



# 1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

class LRUCache: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.front = ListNode(None,None) # Dummy front/back 
        self.back = ListNode(None,None) 
        self.head = self.front
        self.tail = self.back
        self.head.next = self.head
        self.tail.prev = self.tail
        
# 2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
    def int_get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        else:
            return -1
        
            
# 3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add 
# the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
# evict the least recently used key.   

    def void_put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict_least_recent()
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


# additional functions to manipulate nodes within the List 
# (basically used for functionality within our main functions GET & PUT).
    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _evict_least_recent(self):
        last_node = self.tail.prev
        del self.cache[last_node.key]
        self._remove_node(last_node)
        

print(LRUCache())