from sort import seletion_sort, bubble_sort, quick_sort

arr = [2,42,84,5,113,4,6,33,65,756]

sorted = [2, 4, 5, 6, 33, 42, 65, 84, 113, 756]
reversed = [756, 113, 84, 65, 42, 33, 6, 5, 4, 2]

sorted_arr = seletion_sort(arr)

assert(sorted_arr == sorted)

reversed_arr = seletion_sort(arr, True)
assert(reversed_arr == reversed)

sorted_arr = bubble_sort(arr)
assert(sorted_arr == sorted)

reversed_arr = bubble_sort(arr, True)
assert(reversed_arr == reversed)


sorted_arr = quick_sort(arr)
assert(sorted_arr == sorted)

reversed_arr = quick_sort(arr, True)
assert(reversed_arr == reversed)
