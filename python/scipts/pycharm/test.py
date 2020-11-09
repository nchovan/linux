'''
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"Total: {total}")
'''
'''
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')
'''
'''
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

# or you can do it this way

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
'''
'''
numbers = [3, 6, 3, 1, 7, 10, 25, 89, 150, 77, 21, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
'''
'''
2d list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20   # changes the 2 in the first list to 20
print(matrix[0][1])    # first [] is the first list in the matrix and the second [] is the index of that list which is 2
for row in matrix:  # print all items in a matrix
    for item in row:
        print(item)
'''
'''
customer = {
    "name": "nick",
    "age": 35,
    "is_verified": True
}
print(customer.get("name"))
print(customer)
'''
'''
phone = input("phone: ")
digit_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
output = ""
for char in phone:
    output += digit_mapping.get(char, "!") + " "
print(output)
'''
'''
def greet_user(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print('Hope your having a good day')


greet_user('nick', 'chovan')
'''
'''
def square(number):
    return number * number

print(square(3))
'''

