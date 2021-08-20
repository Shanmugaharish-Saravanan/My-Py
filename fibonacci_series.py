#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
nterm = int(input("Enter number here : "))
n1, n2 = 0, 1
total = 0

if nterm <= 0:
    print("Enter postitive number")
elif nterm == 1:
    print("Fibonacci sequence is", nterm, ":")
    print(n1)

else:
    print('Fibonacci series is:')
    while total < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        total += 1
