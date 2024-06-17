# Task 1
def number_generator(numbers):
    for number in numbers:
        yield number

# Task 2
def even_number_generator(start, end):
    for number in range(start, end+1):
        if number % 2 == 0:
            yield number

# Task 3
def odd_number_generator(start, end):
    for number in range(start, end+1):
        if number % 2 != 0:
            yield number

# Task 4
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_number_generator(limit):
    for number in range(2, limit+1):
        if is_prime(number):
            yield number

# Task 6, 7, 8, 9, 10: These tasks require TreeNode and graph implementations, which are not provided. You need to define them to proceed.

# Task 11
def dict_keys_generator(dictionary):
    for key in dictionary.keys():
        yield key

# Task 12
def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

# Task 13
def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

# Task 14
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 15
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16
def string_chars_generator(string):
    for char in string:
        yield char

# Task 17
def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            yield item
            seen.add(item)

# Task 18
def reverse_list_generator(lst):
    for item in reversed(lst):
        yield item

# Task 19
def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

# Task 20
from itertools import permutations

def permutations_generator(lst):
    for perm in permutations(lst):
        yield perm

# Task 21
from itertools import combinations

def combinations_generator(lst):
    for r in range(1, len(lst)+1):
        for combo in combinations(lst, r):
            yield combo

# Task 22
def tuple_list_generator(lst):
    for item in lst:
        yield item

# Task 23
def parallel_lists_generator(*lists):
    min_length = min(len(lst) for lst in lists)
    for i in range(min_length):
        yield tuple(lst[i] for lst in lists)

# Task 24
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

# Task 25
def nested_dict_generator(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

# Task 26
def powers_of_two_generator(n):
    for i in range(n+1):
        yield 2 ** i

# Task 27
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Task 28
def squares_generator(start, end):
    for number in range(start, end+1):
        yield number ** 2

# Task 29
def cubes_generator(start, end):
    for number in range(start, end+1):
        yield number ** 3

# Task 30
def factorials_generator(n):
    factorial = 1
    for i in range(n+1):
        yield factorial
        factorial *= i + 1

# Task 31
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    yield 1

# Task 32
def geometric_progression_generator(initial, ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= ratio

# Task 33
def arithmetic_progression_generator(initial, difference, limit):
    term = initial
    while term <= limit:
        yield term
        term += difference

# Task 34
def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

# Task 35
def running_product_generator(numbers):
    product = 1
    for number in numbers:
        product *= number
        yield product
