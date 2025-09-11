# hpylib

**hpylib** is a small Python library that provides simple building blocks for parallel programming with threads. It is designed to make it easy to run tasks asynchronously, coordinate them, and perform parallel map operations, all with minimal boilerplate.  

It provides three main functions:

1. **`spawn(fn)`** — run a function asynchronously in a worker thread.  
2. **`finish()`** — context manager to wait for all asynchronous tasks submitted inside its block.  
3. **`pmap(fn, iterable)`** — parallel map: apply a function to each element of an iterable in parallel, returning the results as a list.

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