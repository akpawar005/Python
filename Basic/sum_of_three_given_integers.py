#Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def sum_three(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum

a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
c=int(input("enter 3rd number :"))
d=sum_three(a,b,c)
print("The sum of three value is :" ,d)
