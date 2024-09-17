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
