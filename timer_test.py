from timer import Timer

t = Timer(1, 2, 3)

assert(hasattr(t, "hours"))
assert(hasattr(t, "minutes"))
assert(hasattr(t, "seconds"))
assert(t.hours == 1)
assert(t.minutes == 2)
assert(t.seconds == 3)
t.hours = 0
t.minutes = 0
t.seconds = 0

t.tick()
assert(t.hours == 0)
assert(t.minutes == 0)
assert(t.seconds == 1)

t.tick()
assert(t.hours == 0)
assert(t.minutes == 0)
assert(t.seconds == 2)

t.seconds = 59
assert(t.hours == 0)
assert(t.minutes == 0)
assert(t.seconds == 59)
t.tick()
assert(t.hours == 0)
assert(t.minutes == 1)
assert(t.seconds == 0)

t.seconds = 59
t.minutes = 59
assert(t.hours == 0)
assert(t.minutes == 59)
assert(t.seconds == 59)
t.tick()
assert(t.hours == 1)
assert(t.minutes == 0)
assert(t.seconds == 0)

t.seconds = 59
t.minutes = 59
assert(t.hours == 1)
assert(t.minutes == 59)
assert(t.seconds == 59)
t.tick()
assert(t.hours == 2)
assert(t.minutes == 0)
assert(t.seconds == 0)

t.reset()
assert(t.hours == 0)
assert(t.minutes == 0)
assert(t.seconds == 0)

t.hours = 1
t.minutes = 2
t.seconds = 3
assert(t.__str__() == "1h 2m 3s")
