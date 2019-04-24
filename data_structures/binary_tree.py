from dataclasses import dataclass, field

@dataclass
class Node:
    data: int
    left:'Node'
    right:'Node'

    def insert(self, node):
        if self.data > node.data:
            if self.left == None:
                self.left = node
            else:
                self.left.inesrt(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(node)

    def delete(self, node):
        if node == None:
            return None
        if self.data > node.data:
            self.left = self.left.delete(node)
            return node
        elif self.data < node.data:
            self.right = self.right.delete(node)
            return node
        else:
            if self.left == None and self.right == None:
                return None
            elif node.left != None and self.right == None:
                return node.left
            elif node.left == None and self.right != None:
                return node.right
            else:
                min = self.deletemin(self.right)

    def deletemin(self, node):
        if node.left == None:
            if self.left.data == node.data:
                self.left = node.right
            else:
                self.right = node.right
            return node
        else:
            return node.deletemin(node.left)

    def __str__(self):
        return str([self.data, str(self.left), str(self.right)])


@dataclass
class BinaryTree:
    root:Node

    def insert(self, node):
        self.root.insert(node)

    def delete(self, node):
        return self.root.delete(node)

    def __str__(self):
        return str(self.root)

def make_node(value):
    return Node(value, None, None)

binary_tree = BinaryTree(make_node(3))
import pdb; pdb.set_trace()
