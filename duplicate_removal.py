def remove_duplicates(arr):
    if not arr:
        return arr

    unique_idx = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[unique_idx]:
            unique_idx += 1
            arr[unique_idx] = arr[i]

    return arr[:unique_idx + 1]

# Example usage:
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
unique_array = remove_duplicates(array)
print(unique_array)
