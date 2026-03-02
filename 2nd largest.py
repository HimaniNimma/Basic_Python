#2nd highest number using list
H=list(map(int,input("Enter element to the list").split()))
H.sort()
print("The 2nd largest ele is :",H[len(H)-2])

