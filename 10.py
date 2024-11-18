sum_numbers = 0
count = 0

while True:
    num = int(input("Enter an integer (0 to finish): "))
    
    if num == 0:
        break
    
    sum_numbers += num
    count += 1

if count > 0:
    average = sum_numbers / count
    print(f"Sum: {sum_numbers}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")
