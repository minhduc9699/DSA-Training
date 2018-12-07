class BNode:
  def __init__(self, val=None, left=None, right=None):
    self.content = val
    self.left = left
    self.right = right

  def __str__(self):
    strings = ""
    if self.content is not None:
      strings += f"{str(self.content)}"
    if self.left is not None:
      strings += f"L{str(self.left)}"
    if self.right is not None:
      strings += f"R{str(self.right)}"
    if strings == "":
      return "<<E>>"
    else:
      return strings

 
class BTree:
  def __init__(self, val=None):
    self.root = BNode(val)

  def __str__(self):
    return str(self.root)

  def add(self, val, root=None):
    if root is None:
      current_root = self.root
    else:
      current_root = root
    new_node = BNode(val)

    if current_root.content is None:
      self.root = new_node
    elif new_node.content < current_root.content:
      if current_root.left is None:
        current_root.left = new_node
      else:
        self.add(val, current_root.left)
    elif new_node.content > current_root.content:
      if current_root.right is None:
        current_root.right = new_node
      else:
        self.add(val, current_root.right)

  # def _add(self, root, new_node):
  #   if new_node.content < root.content:
  #       if root.left is None:
  #         root.left = new_node
  #       else:
  #         self._add(root.left, new_node)
  #   elif new_node.content > root.content:
  #     if root.right is None:
  #       root.right = new_node
  #     else:
  #       self._add(root.right, new_node)

  def find(self, val):
    node = self.root
    while node is not None:
      if node.content == val:
        return node
      elif val < node.content:
        node = node.left
      else:
        node = node.right
   

if __name__ == "__main__":
    tree = BTree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    tree.add(13)
    tree.add(1)


    # t = tree.find(11)

