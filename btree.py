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

  def add(self, val):
    new_node = BNode(val)
    if self.root.content is None:
      self.root = new_node
    else:
      self._add(self.root, new_node)
  
  def _add(self, root, new_node):
    if new_node.content < root.content:
        if root.left is None:
          root.left = new_node
        else:
          self._add(root.left, new_node)
    elif new_node.content > root.content:
      if root.right is None:
        root.right = new_node
      else:
        self._add(root.right, new_node)

  def find(self, val):
    node = self.root
    found = False
    while node is not None and not found :
      if node.content == val:
        found = True
        return node
      else: 
        if val < node.content:
          node = node.left
        else:
          node = node.right
   

if __name__ == "__main__":
    tree = BTree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    tree.add(13)

    print(tree)
    t = tree.find(11)
    print(t)

