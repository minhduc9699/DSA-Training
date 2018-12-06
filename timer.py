class Timer:
  def __init__(self, hours, mins, secs):
    self.hours = hours
    self.minutes = mins
    self.seconds = secs

  def __str__(self):
    return f"{str(self.hours)}h {str(self.minutes)}m {str(self.seconds)}s"

  def tick(self):
    if self.seconds < 59:
      self.seconds += 1
    else:
      self.seconds = 0
      if self.minutes < 59:
        self.minutes += 1
      else:
        self.minutes = 0
        self.hours += 1

  def reset(self):
    self.seconds = 0
    self.minutes = 0
    self.hours = 0


if __name__ == "__main__":
      
  t = Timer(59, 59, 59)
  print(t)
  print("start")
  t.tick()
  print(t)
    

  
