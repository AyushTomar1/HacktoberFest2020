def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

x = int(input("Enter The number "))
r = fact(x)
print("The Factorial of number is " , r)
