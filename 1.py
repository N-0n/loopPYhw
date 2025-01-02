
num=input("Enter a positive integer : ")
tot=0 
while num>0:
    x=len(num)
    z=0
    for count in range(1,x):
        substr=0
        substr=num(z)
        tot=tot+int(substr)**int(substr)
        count=count+1
        num(z+1)
    if tot==int(num):
        print("The number is an Armstrong number")
    else:
        print("The number isn't an Armstrong number")
else:
    print("The integer should be positive.")
