import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, array_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)

        if element_idx + 1 < len(arrays[array_idx]):
            next_val = arrays[array_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, array_idx, element_idx + 1))

    return result

# Example usage:
arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
merged_array = merge_k_sorted_arrays(arrays)
print(merged_array)
