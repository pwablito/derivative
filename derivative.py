#!/usr/bin/python
import sys
import math
def derivative():
    print('Is the function 1: polynomial 2:trigonometric 3:exponential or 4:logarithmic?')
    type = int(sys.stdin.readline())
    if type == 1:
        print('What is the degree of the polynomial?')
        deg = int(sys.stdin.readline())
        if deg == 0:
            print('0')
        if deg == 1:
            print('What is the coefficient of x?')
            x1 = int(sys.stdin.readline())
            print(x1)
        if deg == 2:
            print('What is the coefficient of x^2?')
            x2 = int(sys.stdin.readline())
            print('What is the coefficient of x?')
            x1 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            print((x2*2*x)+x1)
        if deg == 3:
            print('What is the coefficient of x^3?')
            x3 = int(sys.stdin.readline())
            print('What is the coefficient of x^2?')
            x2 = int(sys.stdin.readline())
            print('What is the coefficient of x?')
            x1 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            print((3*x3*x*x)+(x2*2*x)+x1)
        if deg == 4:
            print('What is the coefficient of x^4?')
            x4 = int(sys.stdin.readline())
            print('What is the coefficient of x^3?')
            x3 = int(sys.stdin.readline())
            print('What is the coefficient of x^2?')
            x2 = int(sys.stdin.readline())
            print('What is the coefficient of x?')
            x1 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            print((4*x4*x*x*x)+(3*x3*x*x)+(x2*2*x)+x1)
        if deg == 5:
            print('What is the coefficient of x^5?')
            x5 = int(sys.stdin.readline())
            print('What is the coefficient of x^4?')
            x4 = int(sys.stdin.readline())
            print('What is the coefficient of x^3?')
            x3 = int(sys.stdin.readline())
            print('What is the coefficient of x^2?')
            x2 = int(sys.stdin.readline())
            print('What is the coefficient of x?')
            x1 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            print((5*x5*x*x*x*x)+(4*x4*x*x*x)+(3*x3*x*x)+(x2*2*x)+x1)
        else:
            print('Powers 1, 2, 3, 4, and 5 are the only acceptable options')
            derivative()
    if type == 2:
        print('Is the function 1: sin(x) 2: cos(x) or 3: tan(x)?')
        t_type = int(sys.stdin.readline())
        if t_type == 1:
            print('What is the coefficient of the sine function?')
            x1 = int(sys.stdin.readline())
            print('What is the coefficient of the x term?')
            x2 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            x3 = x*x2
            print(x1*x2*math.cos(x3))
        if t_type == 2:
            print('What is the coefficient of the cosine function?')
            x1 = int(sys.stdin.readline())
            print('What is the coefficient of the x term?')
            x2 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            x3 = x*x2
            print(x1*x2*math.sin(x3))
        if t_type == 3:
            print('What is the coefficient of the tangent function?')
            x1 = int(sys.stdin.readline())
            print('What is the coefficient of the x term?')
            x2 = int(sys.stdin.readline())
            print('Derivative at what value of x?')
            x = int(sys.stdin.readline())
            x3 = x*x2
            print((float(1)/math.cos(x3))*(float(1)/math.cos(x3))*x1*x2)
        else:
            print('Only 1, 2, and 3 are acceptable inputs.')
            derivative()
    if type == 3:
        print('What is the coefficient of the exponential function?')
        x1 = int(sys.stdin.readline())
        print('What is the base of the exponent?')
        x2 = int(sys.stdin.readline())
        print('What is the coefficient of the exponent?')
        x3 = int(sys.stdin.readline())
        print('Derivative at what value of x?')
        x = int(sys.stdin.readline())
        x4 = x*x3
        print(x3*x1*math.pow(x2, x4)*math.log(x2))
    if type == 4:
        print('What is the coefficient of the logarithmic function?')
        b = int(sys.stdin.readline())
        print('What is the base of the logarithm?')
        a = int(sys.stdin.readline())
        print('Derivative at what value of x?')
        x = int(sys.stdin.readline())
        print(float(b)/float(x*math.log(a)))
    else:
        print('Enter 1, 2, 3, or 4.')
        derivative()


derivative()
