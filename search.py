def linear_search(list, val):
  index = 0
  found = False
  while index < len(list) and not found:
    if list[index] == val:
      found = True
      break
    else:
      index += 1
  return found


def binary_search(list, val):
  lower = 0
  upper = len(list)
  while lower < upper:
    mid = (lower + upper) // 2
    current_val = list[mid]
    if val == current_val:
      return True
    elif val < current_val:
      upper = mid
    else:
      if lower == mid:
        return False
      lower = mid

