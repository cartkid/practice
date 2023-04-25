import random
from typing import List, Union


# Node definition
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def fetch_random_node(head: Node) -> Node:
    nodes: List[Node] = []
    curr_node: Union[Node, None] = head

    while curr_node is not None:
        nodes.append(curr_node)
        curr_node = curr_node.next

    return random.choice(nodes)


def create_nodes(head, nodes):
    for val in nodes:
        new_node = Node(val)
        head.next = new_node
        head = new_node


def list_to_str(head):
    new_str = ""
    while head:
        new_str += str(head.val)
        head = head.next
    return new_str
