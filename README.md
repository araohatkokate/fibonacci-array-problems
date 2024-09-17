# fibonacci-array-problems
## Problem 0: Fibonacci sequence problem
### Step by Step call stack for fib(5):
- `fib(5)`
  - `fib(4)`
    - `fib(3)`
      - `fib(2)`
        - `fib(1)`-> returns 1
        - `fib(0)` → returns 0  
      - returns `1 + 0 = 1`  
      - `fib(1)` → returns 1  
    - returns `1 + 1 = 2`  
    - `fib(2)`  
      - `fib(1)` → returns 1  
      - `fib(0)` → returns 0  
    - returns `1 + 0 = 1`  
  - returns `2 + 1 = 3`  
  - `fib(3)`  
    - `fib(2)`  
      - `fib(1)` → returns 1  
      - `fib(0)` → returns 0  
    - returns `1 + 0 = 1`  
    - `fib(1)` → returns 1  
  - returns `1 + 1 = 2`  
- returns `3 + 2 = 5`
### Call Stack Trace:
- fib(5) → fib(4) → fib(3) → fib(2) → fib(1)
- fib(5) → fib(4) → fib(3) → fib(2) → fib(0)
- fib(5) → fib(4) → fib(3) → fib(1)
- fib(5) → fib(4) → fib(2) → fib(1)
- fib(5) → fib(4) → fib(2) → fib(0)
- fib(5) → fib(3) → fib(2) → fib(1)
- fib(5) → fib(3) → fib(2) → fib(0)
- fib(5) → fib(3) → fib(1)

### Time Complexity of Fibonacci:
**Recursive Fibonacci**: The time complexity is \( O(2^n) \), where \( n \) is the input number. This exponential growth occurs because each Fibonacci number requires the calculation of the two preceding numbers, resulting in many redundant recursive calls.

### Improvements:
1. **Memoization**: Storing previously computed Fibonacci values to avoid redundant calculations. This reduces the time complexity to \( O(n) \).
2. **Iterative approach**: A simple loop to calculate Fibonacci can further reduce overhead by avoiding recursion altogether, making the time complexity \( O(n) \).

### Debugging Steps:
1. **Ensure code is set up for debugging**
2. **Set up a debug configuration**
3. **Set breakpoint on the "return fib(n-1) + fib(n-2)" line**
4. **Start debugging**
5. **Observe the call stack**

## Problem 1: Merging K Sorted Arrays
### Implementation : In k_sorted_arrays.py file
### Time Complexity :

Inserting into and removing from the heap both take \( O(log K) \), where \( K \) is the number of arrays.  
Since we process every element in each array, the total number of elements is \( N X K \). For each element, we perform a heap operation.

Hence, the time complexity is \( O(N X K log K) \).

### Improvements :

- **Optimizing the Heap Structure**: You could experiment with more advanced heap structures such as a **Fibonacci heap**, but the practical gain may not be significant for typical inputs.
- **Parallel Processing**: If the arrays are large, you could explore parallelizing the merge operation for further performance improvement.

## Problem 2: Removing duplicates from sorted array
### Time Complexity :

The algorithm only requires one pass through the array, so the time complexity is \( O(N) \), where \( N \) is the size of the array.

### Improvements :

- **Memory Usage**: This algorithm is already optimal in terms of memory since it operates in-place.
- **Early Exit Optimization**: If the input array is very large and contains few duplicates, you could add a condition to exit early if no duplicates are found after some point.



