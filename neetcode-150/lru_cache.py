# Time: O(N) for get() and put() 
# Space: O(N)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # key -> node to access nodes in O(1) time
        self.mapping = {}
        # dummy nodes to avoid handling edge cases separately
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # doubly linked list to delete/add nodes in O(1) time
        # we keep the nodes in the order of most recently used to least recently used from left to right
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.mapping:
            node = self.mapping[key]
            # as we touched this node, it becomes a recently used node so we bring it to the front of the list
            self.deleteNode(node)
            self.addToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            node = Node(key, value)
            self.mapping[key] = node
            # if we have reached the max capacity then we can delete the last node as it was least recently used
            if self.capacity <= 0:
                del self.mapping[self.tail.prev.key]
                self.deleteNode(self.tail.prev)
                # the new node should be added at head as it is most recently used
                self.addToHead(node)
            else:
                # reduce the capacity only when we add a new node
                self.capacity -= 1
                self.addToHead(node)
        
