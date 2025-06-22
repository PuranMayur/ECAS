from node import Node

def comp_1(node_1, node_2):
    if node_1.key < node_2.key:
        return False
    elif node_1.key > node_2.key:
        return True
    elif node_1.value < node_2.value:
        return False
    else:
        return True

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_height(self, node):
        return node.height if node else -1

    def update_height(self, node):
        if node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            self.size += 1
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def _min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._min_value_node(node.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                self.size -= 1
                return temp
            elif not node.right:
                temp = node.left
                node = None
                self.size -= 1
                return temp

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        self.update_height(node)
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def search(self, key, return_key=False):
        result = self._search(self.root, key, return_key)
        if result is None:
            return None
        return result.key if return_key else result.value
    
    def _search(self, node, key, return_key):
        if not node or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key, return_key)
        return self._search(node.right, key, return_key)
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

class BinLocatorAVL:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.size += 1
        else:
            self.root = self._insert(self.root, key, value)
            self.size += 1
    
    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        temp_node = Node(key, value)
        if self.comparator(node, temp_node):
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
    
    def _balance(self, node):
        if self._get_balance(node) > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if self._get_balance(node) < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node
    
    def _rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))
        return temp
    
    def _rotate_right(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))
        return temp
    
    def _get_height(self, node):
        if node is None:
            return -1
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def search(self, key, value):
        return self._search(self.root, key, value)
    
    def _search(self, node, key, value):
        if node is None:
            return None
        if node.key == key and node.value == value:
            return node
        if self.comparator(node, Node(key, value)):
            return self._search(node.left, key, value)
        else:
            return self._search(node.right, key, value)

    def delete(self, key, value):
        self.root = self._delete(self.root, key, value)
    
    def _delete(self, node, key, value):
        if node is None:
            return None
        if node.key == key and node.value == value:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key, temp.value)
        elif self.comparator(node, Node(key, value)):
            node.left = self._delete(node.left, key, value)
        else:
            node.right = self._delete(node.right, key, value)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def min_greater_than_eq(self, key, least_id=True):
        return self._min_greater_than_eq(self.root, key, least_id)

    def _min_greater_than_eq(self, node, key, least_id):
        if node is None:
            return None
        if node.key >= key:
            left_result = self._min_greater_than_eq(node.left, key, least_id)
            if left_result is not None:
                return left_result
            if least_id:
                return node
            else:
                temp = node.key
                return self.greatest_id(temp)
        return self._min_greater_than_eq(node.right, key, least_id)
    
    def least_id(self, key):
        return self._least_id(self.root, key)
    
    def _least_id(self, node, key):
        if node is None:
            return None
        if node.key == key:
            left_result = self._least_id(node.left, key)
            if left_result is not None:
                return left_result
            return node
        elif node.key > key:
            return self._least_id(node.left, key)
        else:
            return self._least_id(node.right, key)
        
    def greatest_id(self, key):
        return self._greatest_id(self.root, key)
    
    def _greatest_id(self, node, key):
        if node is None:
            return None
        if node.key == key:
            right_result = self._greatest_id(node.right, key)
            if right_result is not None:
                return right_result
            return node
        elif node.key > key:
            return self._greatest_id(node.left, key)
        else:
            return self._greatest_id(node.right, key)  
    
    def largest(self, least_id=True):
        return self._largest(self.root, least_id)
    
    def _largest(self, node, least_id):
        if node.right is None:
            temp = node.key
            if least_id:
                return self.least_id(temp)
            else:
                return self.greatest_id(temp)
        return self._largest(node.right, least_id)

    def print_tree(self):
        lines = []
        self._print_tree(self.root, "", True, lines)
        for line in lines:
            print(line)

    def _print_tree(self, node, prefix, is_tail, lines):
        if node.right is not None:
            new_prefix = prefix + ("│   " if is_tail else "    ")
            self._print_tree(node.right, new_prefix, False, lines)
        lines.append(prefix + ("└── " if is_tail else "┌── ") + f"({node.key}, {node.value})")
        if node.left is not None:
            new_prefix = prefix + ("    " if is_tail else "│   ")
            self._print_tree(node.left, new_prefix, True, lines)