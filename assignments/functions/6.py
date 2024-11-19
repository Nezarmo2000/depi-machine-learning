x=int(input("Enter the first number in series is "))
y=int(input("Enter the last number in series is "))
num_even=0
num_odd=0
for i in range(x,y+1):
    if i%2==0:
        num_even+=1
    else :
        num_odd+=1
print(f"Number  of even numbers is {num_even}" )
print(f"Number of odd numbers is {num_odd}" )