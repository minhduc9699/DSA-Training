class Node:
  def __init__(self, val=None, next=None):
    self.content = val
    self.next = next
  
  def __str__(self):
    if self.next is None:
      return str(self.content)
    else:
      return f"{str(self.content)}->{str(self.next)}"
  

class LinkedList:
  def __init__(self, head=None, tail=None):
    self.head = head
  
  def __str__(self):
    if self.head is None:
      return "<<E>>"
    else:
      return str(self.head)


  def add_first(self, val):
    new_node = Node(val)
    new_node.next = self.head
    self.head = new_node

  def add_last(self, val):
    new_node = Node(val)
    if self.head is not None:
      current_node = self.head
      while current_node.next != None:
        current_node = current_node.next
      current_node.next = new_node
    else:
      self.add_first(val)
  
  def remove_first(self):
    if self.head is not None:
      self.head = self.head.next
    else:
      pass
  
  def remove_last(self):
    if self.head is not None:
      current_node = self.head
      last_note = self.head
      while current_node.next is not None:
        last_note = current_node
        current_node = current_node.next
      if self.head.next is None:
        self.head = None
      last_note.next = None
    else:
      pass
  
  def find(self, val):
    current_node = self.head
    node_found = False
    while current_node.next is not None and not node_found:
      if current_node.content == val:
        node_found = True
        return current_node
      else:
        current_node = current_node.next
    return None

    







