class Fraction:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f"{str(self.x)} / {str(self.y)}"

  def add(self, dx, dy):
    if self.y == dy:
      self.x += dx
    else:
      numerator = self.x * dy + self.y * dx
      denominator = self.y * dy 
      self.x = numerator
      self.y = denominator

  def subtract(self, dx, dy):
    if self.y == dy:
      self.x -= dx
    else:
      numerator = self.x * dy - self.y * dx
      denominator = self.y * dy
      self.x = numerator
      self.y = denominator

  def multiply(self, dx, dy):
    self.x *= dx
    self.y *= dy

  def divide(self, dx, dy):
    self.x /= dx
    self.y /= dy

  def minimize(self):
    def gcd(a, b):
      # if b == 0:
      #   return a
      # else:
      #   return gcd(b, a%b)
      #or...
      if a == 0:
        return b
      if b == 0:
        return a
      if a > b:
        return gcd(a-b, b)
      return gcd(a, b-a)


    num = gcd(self.x, self.y)
    self.x /= num
    self.y /= num    
