"""Task 2"""

# def fizzbuzz(maximum_value):
#     for n in range(maximum_value):
#         if n % 5 == 0 and n % 3 == 0:
#             print('FizzBuzz')
#         elif n % 5 == 0:
#             print('Buzz')
#         elif n % 3 == 0:
#             print('Fizz')
#         else:
#             print(n)
            

# fizzbuzz(31)



"""Task 3"""


def get_n(n, memoize={1: 1, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_n(n - 1, memoize) + get_n(n-2, memoize)
    return memoize[n]

r = get_n(10)

print(r)


# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# result = fibonacci(5)

# print(result)


# def fibonacci_two(n):
    
#     a, b = 0, 1
#     index = 0
#     while index < n:
#         a, b = b, a + b
#         index += 1
#         print(a)


# fibonacci_two(10)
