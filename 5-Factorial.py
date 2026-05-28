h=int(input("Enter num"))
if(h==0):
    print(f"Factorial of {h} is 0")
else:
    result=1
    for i in range(1,h+1):
        result=result*i
print(f"Factorial of {h} is {result}")
