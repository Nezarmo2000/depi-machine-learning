text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"The number of vowels in the string is: {count}")

"""
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
num =list(filter(lambda char: char in vowels, text))
print(f"The number of vowels in the string is: {len(num)}")
"""
