class Queue:
  def __init__(self):
    self.items = []

  def __str__(self):
    items_string = ""
    white_space = " "
    for i in range(len(self.items)):
      if i == len(self.items) - 1:
        white_space = ""
      items_string += str(self.items[i]) + white_space

    return str(items_string)

  def insert(self, val):
    return self.items.insert(0, val)

  def remove(self):
    if self.is_empty():
      return None
    else:
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0
  
if __name__ == "__main__":
    q = Queue()
    print(q)
    q.insert(10)
    print(q)
    q.insert(5)
    print(q)
    q.remove()
    print(q)
