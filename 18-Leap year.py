#Finding whether the year is Leap Year or not
year = int(input("Enter year"))
if ((year%400)==0) or ((year%4==0)and(year%100!=0)):
    print("True")
else:
    print("False")
