#!usr/bin/python3
def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            arr[slow] = arr[fast]

    return slow + 1

arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(arr)
print(new_length, arr[:new_length])
