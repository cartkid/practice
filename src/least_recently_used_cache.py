from typing import Union


class ListNode:
    def __init__(self, key, value=-1):
        self.key = key
        self.value = value
        self.prev: Union[ListNode, None] = None
        self.next: Union[ListNode, None] = None


class Cache:
    def __init__(self, capacity: int):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> Union[int, None]:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return None

    def put(self, key: int, value: int) -> None:
        if key in self.dic:  # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value  # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node: ListNode):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        if headNext is not None:
            headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.prev
        if tail_node is not None:
            del self.dic[tail_node.key]
        self.removeFromList(tail_node)

    def print(self):
        curr = self.head
        print(f"SUMMARY: {len(self.dic)} of {self.capacity}")
        while curr.next is not None:
            print(
                f"{curr.key if curr.key is not None else 'START'}: {curr.value if curr.value is not None else '--'}"
            )
            curr = curr.next
        print(
            f"{curr.key if curr.key is not None else 'END  '}: {curr.value if curr.value is not None else '--'}"
        )

    def print_reverse(self):
        curr = self.tail
        print(f"SUMMARY: {len(self.dic)} of {self.capacity}")
        while curr.prev is not None:
            print(
                f"{curr.key if curr.key is not None else 'END  '}: {curr.value if curr.value is not None else '--'}"
            )
            curr = curr.prev
        print(
            f"{curr.key if curr.key is not None else 'Start'}: {curr.value if curr.value is not None else '--'}"
        )
