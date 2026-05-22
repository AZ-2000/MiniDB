class Node:
    def __init__(self, key = 0, val = 0):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class DLL:
    def __init__(self, head = None, tail = None, used = None):
        self.head = head
        self.tail = tail
        self.used = used

    def insert(self, new_node):
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    
    def delete_LRU_Node(self):
        if self.head.next is None:
            self.head = None
        else:
            tmp = self.head.next
            tmp.prev = None
            self.head.next = None
            self.head = tmp

    def LRU_Node(self):
        return self.head
    
    def swap(self, node):
        if node is None:
            return
        elif node.prev is None and node.next is None:
            return
        elif node.prev is None:
            tmp = node.next
            tmp.prev = None
            node.next = None
            self.head = tmp
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        elif node.next is None:
            return
        else:
            prev = node.prev
            nxt = node.next
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            prev.next = nxt
            nxt.prev = prev
            node.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.hashmap = {}
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            self.dll.swap(self.hashmap[key])
            return self.hashmap[key].val
            
    def put(self, key: int, value: int) -> None:
        
        if key not in self.hashmap:    
            self.count += 1 
            if self.count > self.capacity:
                lru_node = self.dll.LRU_Node()
                self.dll.delete_LRU_Node()
                del self.hashmap[lru_node.key]
                self.count -= 1
            new_node = Node(key,value)
            self.dll.insert(new_node)        
            self.hashmap[key] = new_node
        else:
            self.hashmap[key].val = value
            self.dll.swap(self.hashmap[key])

            
        

