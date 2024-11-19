numbers = [4, 2, 9, 7, 1, 5]
minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print(f"The minimum value is: {minimum}")
print(f"The maximum value is: {maximum}")
