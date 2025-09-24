# hpylib

**hpylib** is a small Python library that provides structured parallel programming constructs. It provides three layers of abstraction:

1. **`pmap(fn, iterable)` and `pfilter(fn, iterable)`** — parallel map and filter.  
2. **`finish()` and `spawn(fn)`** — `finish` waits for all tasks submitted inside its block to complete, and `spawn` submits a task to run in a worker thread.
3. **`async_future(fn)`** — submit a task to run asynchronously and return a future.

Layer 1 is the highest level of abstraction, and it does not have explicit tasks. It simply applies a function to each element of an iterable in parallel. Layer 2 spawns tasks to run asynchronously, but does not have explicit joins. Layer 3 is the lowest level of abstraction, and it allows explicit task creation and joining.


---

## Installation

```bash
pip install hpylib
```

---

## Usage

### 1. Asynchronous Tasks with `spawn` and `finish`

```python
from hpylib import spawn, finish
import time

def work(x):
    time.sleep(1)
    print(f"Processed {x}")

with finish():
    for i in range(5):
        spawn(lambda i=i: work(i))

print("All tasks completed!")

```

* spawn(fn) submits a task to run in the background.

* finish() waits for all tasks submitted inside its block to complete.

### 2. Parallel Map with `pmap`

```python
from hpylib import pmap
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 100_000)
results = pmap(is_prime, numbers)
total_primes = sum(results)
print(f"Number of primes: {total_primes}")

```

* pmap(fn, iterable) automatically splits the iterable into chunks and distributes the work across the thread pool.

* Returns a list of results in the same order as the input.

* Blocks until all tasks are complete.