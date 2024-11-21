start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Prime numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number)
