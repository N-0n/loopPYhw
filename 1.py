
num=int(input("Enter a positive integer : "))
tot=0

if num>0 :
    y=str(num)
    x=len(y)
    for count in range(0,x):
        substr=y[count]
        tot+=int(substr)**x   
    if tot==num:
        print("The number is an Armstrong number")
    else:
        print("The number isn't an Armstrong number")
else:
    print("The number isn't a positive integer")