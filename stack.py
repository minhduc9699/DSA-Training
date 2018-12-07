class Stack:
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

  def is_empty(self):
    return len(self.items) == 0

  def push(self, value):
    self.items.append(value)

  def pop(self):
    if self.is_empty():
      pass
    else:
      return self.items.pop()

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push("5")
    s.push("5")
    print(s.is_empty())
