def seletion_sort(arr, reversed=False):
  for i in range(len(arr)-1):
    min_index = i
    min_val = arr[min_index]
    for j in range(i+1, len(arr)):
      if reversed:
        if arr[j] > min_val:
          min_index = j
          min_val = arr[j]
      else:
        if arr[j] < min_val:
          min_index = j
          min_val = arr[j]
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr


def bubble_sort(arr, reversed=False):
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if reversed:
        if arr[i] < arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
      else:
         if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
  return arr


def quick_sort(arr, reversed=False):
  left = []
  equal = []
  right = []
  if len(arr) > 1:
    pivot = arr[0]
    for i in arr:
      if not reversed:
        if i < pivot:
          left.append(i)
        elif i > pivot:
          right.append(i)
        else:
          equal.append(i)
      else:
        if i > pivot:
          left.append(i)
        elif i < pivot:
          right.append(i)
        else:
          equal.append(i)
    return quick_sort(left, reversed) + equal + quick_sort(right, reversed)
  else:
    return arr

arr = [5, 4, 3, 1, 6, 8, 10, 9]