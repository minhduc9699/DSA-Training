class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({str(self.x)},{str(self.y)})"

  def add(self, dx, dy):
    self.x += dx
    self.y += dy

  def subtract(self, dx, dy):
    self.x -= dx
    self.y -= dy

  def scale(self, num):
    self.x *= num
    self.y *= num

  def get_length(self):
    return (self.x**2 + self.y**2)**0.5

