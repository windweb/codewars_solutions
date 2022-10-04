# Beginner Series #3 Sum of Numbers

**Description:**

Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return `a` or `b`.

Note: `a` and `b` are not ordered!

**Examples (a, b) --> output (explanation)**
```
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2) 
```

**Solution:**
```python
def get_sum(a,b):
    result = []
    if a == b:
        return a
    elif a < b:
        for num in range(a, b+1, 1):
            result.append(num)
    elif a > b:
        for num in range(a, b-1, -1):
            result.append(num)
    return sum(result)
```


Codewars source [link](https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python)