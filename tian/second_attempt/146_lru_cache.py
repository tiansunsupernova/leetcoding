class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        
        self.di = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.next = self.head
        self.head.prev = self.tail
        # tail -> n1 -> last_node -> head

    def get(self, key: int) -> int:
        if key in self.di:
            node = self.di[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.di:
            self.remove(self.di[key])
        new_node = Node(key, value)
        self.di[key] = new_node
        self.add(new_node)
        if len(self.di) > self.cap:
            oldest_node = self.tail.next
            del self.di[oldest_node.key]
            self.remove(oldest_node)

    def add(self, node) -> None:
        last_node = self.head.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.head
        self.head.prev = node

    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)