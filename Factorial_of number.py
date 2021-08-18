num = int(input('Enter the num here '))
factorial = 1
if num < 0:
    print ("No negative numbers")
elif num == 0:
    print ("Factor is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
