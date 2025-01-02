
num=input("Enter a positive integer : ")
add=0 
while num>0:
    x=len(num)
    z=0
    for count in range(1,x):
        substr=0
        substr=num(z)
        add=int(substr)**int(substr)
        count=count+1
        num(z+1)
else:
    print("The integer should be positive.")
