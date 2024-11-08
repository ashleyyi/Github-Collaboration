def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(numbers))  # Output: [2, 4, 6, 8, 10]

count = 0

newList = []

while count < 10:
    if numbers[count] % 2 != 0:
        newList.append(numbers[count])

print(newList)