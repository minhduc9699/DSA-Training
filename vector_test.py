from vector import Vector

v = Vector()

#check attr
assert(v is not None)
assert(hasattr(v, "add"))
assert(hasattr(v, "subtract"))
assert(hasattr(v, "scale"))
assert(hasattr(v, "get_length"))

assert(v.x == 0)
assert(v.y == 0)
v.x = 1
v.y = 2
assert(v.x == 1)
assert(v.y == 2)

#check func
v.add(2, 3)
assert(v.x == 3)
assert(v.y == 5)

v.subtract(4, 7)
assert(v.x == -1)
assert(v.y == -2)

v.scale(2)
assert(v.x == -2)
assert(v.y == -4)

v.x = 3
v.y = 4
v_length = v.get_length()
assert(v_length == 5.0)

v.add(2/3, 4/5)

