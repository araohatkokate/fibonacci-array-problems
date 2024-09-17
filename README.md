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
