# Example of creating a binary tree using the TreeNode class with alphabetical naming

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)


def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)


def pre_order_iterative(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def search(node, target):
    if not node:
        return False

    if node == target:
        return True

    return search(node.left, target) or search(node.right, target)


def bfs(node):
    from collections import deque
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


bfs(A)
