from search import linear_search

list = [2, 3, 4, 6, 4, 10, 20]
for num in list:
  s = linear_search(list, num)
  assert(s)

s = linear_search(list, 300)
assert(not s)