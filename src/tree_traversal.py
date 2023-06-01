from typing import List, Union


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children = []

    def add_child(self, child_to_add):
        self.children.append(child_to_add)

    def remove_child(self, child_to_remove):
        self.children = [
            child for child in self.children if child is not child_to_remove
        ]


class Traverse:
    def __init__(self):
        self.preorder: List[int] = []
        self.postorder: List[int] = []

    def preorder_traversal(self, root: TreeNode):
        self.preorder.append(root.value)
        for child in root.children:
            self.preorder_traversal(child)

    def postorder_traversal(self, root: TreeNode):
        for child in root.children:
            self.postorder_traversal(child)
        self.postorder.append(root.value)


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.children = []

    def print(self) -> List[str]:
        menu = TraverseMenu()
        menu.traverse_menu(self)
        return menu.preorder


def _get_stack_to_item(
    item: MenuItem, menu: MenuItem, curr_list: List[MenuItem] = []
) -> Union[List[MenuItem], None]:
    if curr_list == []:
        curr_list = [menu]

    if menu.name == item.name:
        return curr_list

    for child in menu.children:
        curr_list.append(child)
        sub_group_result = _get_stack_to_item(
            item=item, menu=child, curr_list=curr_list
        )
        if sub_group_result is not None and len(sub_group_result) > 0:
            return sub_group_result
        curr_list.pop()


def get_price(menus: List[MenuItem], item: MenuItem) -> Union[float, None]:
    for menu in menus:
        stack_to_item = _get_stack_to_item(item=item, menu=menu)
        while stack_to_item is not None and len(stack_to_item) > 0:
            curr = stack_to_item.pop()
            if curr.price is not None:
                return curr.price


class TraverseMenu:
    def __init__(self):
        self.preorder: List[str] = []

    def traverse_menu(self, item: MenuItem):
        item_as_str: str = (
            f"{item.name} {item.price}" if item.price is not None else item.name
        )
        self.preorder.append(item_as_str)
        for child in item.children:
            self.traverse_menu(child)
