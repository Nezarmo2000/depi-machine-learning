numbers = [10, 20, 30, 50, 40]

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("The maximum value in the list is:", max_value)