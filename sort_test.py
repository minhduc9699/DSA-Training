from sort import seletion_sort, bubble_sort, quick_sort

arr = [2,42,84,5,113,4,6,33,65,756]

sorted_arr = seletion_sort(arr)

assert(sorted_arr == [2, 4, 5, 6, 33, 42, 65, 84, 113, 756])

reversed_arr = seletion_sort(arr, True)
assert(reversed_arr == [756, 113, 84, 65, 42, 33, 6, 5, 4, 2])

sorted_arr = bubble_sort(arr)
assert(sorted_arr == [2, 4, 5, 6, 33, 42, 65, 84, 113, 756])

reversed_arr = bubble_sort(arr, True)
assert(reversed_arr == [756, 113, 84, 65, 42, 33, 6, 5, 4, 2])


sorted_arr = quick_sort(arr)
assert(sorted_arr == [2, 4, 5, 6, 33, 42, 65, 84, 113, 756])

reversed_arr = quick_sort(arr, True)
assert(reversed_arr == [756, 113, 84, 65, 42, 33, 6, 5, 4, 2])
