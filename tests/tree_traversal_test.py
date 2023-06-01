import src.tree_traversal as tree_traversal


def test_tree_traversal0():
    root = tree_traversal.TreeNode(1)
    two = tree_traversal.TreeNode(2)
    two.add_child(tree_traversal.TreeNode(21))
    two.add_child(tree_traversal.TreeNode(22))
    three = tree_traversal.TreeNode(3)
    three.add_child(tree_traversal.TreeNode(31))
    three.add_child(tree_traversal.TreeNode(32))
    three.add_child(tree_traversal.TreeNode(33))
    three.add_child(tree_traversal.TreeNode(34))
    root.add_child(two)
    root.add_child(three)

    traverse = tree_traversal.Traverse()
    traverse.preorder_traversal(root)
    traverse.postorder_traversal(root)

    assert traverse.preorder == [1, 2, 21, 22, 3, 31, 32, 33, 34]
    assert traverse.postorder == [21, 22, 2, 31, 32, 33, 34, 3, 1]


def test_menu_traversal0():
    expected = [
        "Main Menu",
        "Appetizers",
        "Salad 5.99",
        "Soup 4.99",
        "Desserts",
        "Cake 3.99",
        "Ice Cream 2.99",
        "Beverages",
        "Soft Drink 1.99",
        "Coffee 2.49",
    ]

    # Creating the menu tree
    root = tree_traversal.MenuItem("Main Menu", None)

    appetizers = tree_traversal.MenuItem("Appetizers", None)
    appetizers.children.append(tree_traversal.MenuItem("Salad", 5.99))
    appetizers.children.append(tree_traversal.MenuItem("Soup", 4.99))
    root.children.append(appetizers)

    desserts = tree_traversal.MenuItem("Desserts", None)
    desserts.children.append(tree_traversal.MenuItem("Cake", 3.99))
    desserts.children.append(tree_traversal.MenuItem("Ice Cream", 2.99))
    root.children.append(desserts)

    beverages = tree_traversal.MenuItem("Beverages", None)
    beverages.children.append(tree_traversal.MenuItem("Soft Drink", 1.99))
    beverages.children.append(tree_traversal.MenuItem("Coffee", 2.49))
    root.children.append(beverages)

    menu_traversal = tree_traversal.TraverseMenu()
    menu_traversal.traverse_menu(root)

    assert menu_traversal.preorder == expected

    result = root.print()
    assert result == expected


def test_menu_traversal1():
    expected = [
        "Beverages",
        "Soft Drink 1.99",
        "Coffee 2.49",
    ]

    # Creating the menu tree
    root = tree_traversal.MenuItem("Main Menu", None)

    appetizers = tree_traversal.MenuItem("Appetizers", None)
    appetizers.children.append(tree_traversal.MenuItem("Salad", 5.99))
    appetizers.children.append(tree_traversal.MenuItem("Soup", 4.99))
    root.children.append(appetizers)

    desserts = tree_traversal.MenuItem("Desserts", None)
    desserts.children.append(tree_traversal.MenuItem("Cake", 3.99))
    desserts.children.append(tree_traversal.MenuItem("Ice Cream", 2.99))
    root.children.append(desserts)

    beverages = tree_traversal.MenuItem("Beverages", None)
    beverages.children.append(tree_traversal.MenuItem("Soft Drink", 1.99))
    beverages.children.append(tree_traversal.MenuItem("Coffee", 2.49))
    root.children.append(beverages)

    menu_traversal = tree_traversal.TraverseMenu()
    menu_traversal.traverse_menu(beverages)

    assert menu_traversal.preorder == expected

    result = beverages.print()
    assert result == expected


def test_menu_get_price0():
    expected = 2.99

    # Creating the menu tree
    root_empty = tree_traversal.MenuItem("Main Menu Empty", None)
    root = tree_traversal.MenuItem("Main Menu", None)

    appetizers = tree_traversal.MenuItem("Appetizers", None)
    appetizers.children.append(tree_traversal.MenuItem("Salad", 5.99))
    appetizers.children.append(tree_traversal.MenuItem("Soup", 4.99))
    root.children.append(appetizers)

    desserts = tree_traversal.MenuItem("Desserts", None)
    desserts.children.append(tree_traversal.MenuItem("Cake", 3.99))
    desserts_icecream = tree_traversal.MenuItem("Ice Cream", 2.99)
    desserts_icecream_choc = tree_traversal.MenuItem("Chocolate", None)
    desserts_icecream.children.append(desserts_icecream_choc)
    desserts.children.append(desserts_icecream)
    root.children.append(desserts)

    beverages = tree_traversal.MenuItem("Beverages", None)
    beverages.children.append(tree_traversal.MenuItem("Soft Drink", 1.99))
    beverages.children.append(tree_traversal.MenuItem("Coffee", 2.49))
    root.children.append(beverages)

    menu_item_price = tree_traversal.get_price(
        [root_empty, root], tree_traversal.MenuItem(name="Chocolate", price=None)
    )

    assert menu_item_price == expected
