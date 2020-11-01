""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inorder_traversal(root, values) :
    if root is not None:
        inorder_traversal(root.left, values)
        values.append(root.data)
        inorder_traversal(root.right, values)
    # return 'ss'

    
def check_binary_search_tree_(root):
    values = []
    inorder_traversal(root,values)
    
    return len(values) == len(set(values)) and sorted(values) == values  