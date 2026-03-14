# Python 函数

# 普通函数
def greet(name):
    return f"Hello, {name}!"

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 可变参数
def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# 关键字参数
def person_info(name, age, city="北京"):
    return f"{name}, {age}岁, {city}"

# Lambda 函数
square = lambda x: x ** 2
print(f"平方: {square(5)}")

# 高阶函数
numbers = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, numbers))
filtered = list(filter(lambda x: x > 2, numbers))
print(f"映射: {mapped}")
print(f"过滤: {filtered}")

# 递归
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10): {fibonacci(10)}")
