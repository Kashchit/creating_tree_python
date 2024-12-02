# Tree -- construction and traversal

class Tnode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#parent root
root = Tnode(11)

#left
root.left = Tnode(5)
root.left.left = Tnode(7)
root.left.left.right = Tnode(9)

#right 
root.right = Tnode(3)
root.right.left = Tnode(6)
root.right.right = Tnode(8)

#traversal - post order
def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value, end=' ')

#traversal - pre order
def pre_order(root):
    if not root:
        return
    print(root.value, end=' ')
    post_order(root.left)
    post_order(root.right)

#traversal - in order
def in_order(root):
    if not root:
        return
    post_order(root.left)
    print(root.value, end=' ')
    post_order(root.right)

# display
print("Post order:")
post_order(root)

print("\nIn order: ")
in_order(root)

print("\nPre order: ")
pre_order(root)