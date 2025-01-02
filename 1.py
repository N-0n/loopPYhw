num=int(input("Enter a positive integer : "))
tot=0 

x=len(str(num))
z=0
for count in range(0,x):
     substr=0
     substr=num[z]
     tot=tot+(substr**substr)
     num[z+1]

if tot==num:
    print("The number is an Armstrong number")
else:
    print("The number isn't an Armstrong number")
