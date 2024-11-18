reuslt=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        num=i
        reuslt.append(num)
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700: ")
print(reuslt)