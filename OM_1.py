import numpy as np
import matplotlib.pyplot as plt

count = 0

# my function
def f(x):
    global count
    count += 1
    return ((x ** 2 - 4) ** 2) / 6 - 1

# first derivative
def df1(x):
    return ((4 * x ** 3) - 16 * x) / 6

# second derivative
def df2(x):
   return (12 * x ** 2 - 16) / 6

def plotAxes(l, r):
    global count
    axes = plt.gca()
    axes.set_ylim(-3, 30)

    x = np.linspace(l, r, num=100)
    plt.plot(x, f(x), 'k-')
    count = 0

def visualization(x, y):
    plt.plot(x, y, 'md')


# bisection results: 
# minimum value:  1.9999980927
# function was called:  62  times
# number of iterations:  20

# bisection method
def bisection(l, r):
    global count
    count = 0

    xm = (l + r) / 2
    L = r - l

    plotAxes(l, r)
    
    j = 0    
    while (L >= 0.0001):
        x1 = l + L / 4
        x2 = r - L / 4
        f1 = f(x1)
        f2 = f(x2)
        fxm = f(xm)

        visualization(x1, f1)
        visualization(x2, f2)

        if (f1 < fxm):
            r = xm
            xm = x1
        
        elif (f2 < fxm):
            l = xm
            xm = x2

        else:
            l = x1
            r = x2
        
        L = r - l
        j += 1

    plt.plot(xm, f(xm), 'gx')
    plt.show()

    return "%.10f" % xm, count, j

def golden(l, r):
    global count
    count = 0
    j = 0
    phi = 0.61803
    L = r - l
    x1 = r - phi * L
    x2 = l + phi * L
    f1 = f(x1)
    f2 = f(x2)

    plotAxes(l, r)

    while (L >= 0.0001):
        visualization(x1, f1)
        visualization(x2, f2)

        if (f2 < f1):
            l = x1
            L = r - l
            x1 = x2
            x2 = l + phi * L
            f1 = f2
            f2 = f(x2)
        
        else:
            r = x2
            L = r - l
            x2 = x1
            x1 = r - phi * L
            f2 = f1
            f1 = f(x1)

        j += 1

    plt.plot(x1, f(x1), "gx")
    plt.show()

    return "%.10f" % x1, count, j

def newton(x0):
    global count
    count = 0
    j = 0

    curr = x0 - df1(x0) / df2(x0)
    x = x0
    
    plotAxes(0, 10)

    while (abs(x - curr) >= 0.0001):
        visualization(x, f(x))
        visualization(curr, f(curr))

        x = curr
        curr = x - df1(x) / df2(x)
        j += 1

    plt.plot(curr, f(curr), 'gx')
    plt.show()

    return curr, count, j

def main():
    l = 0
    r = 10

    minimum, count, j = bisection(l, r)
    print("bisection results:",
          "\nx value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\niterations: ", j ,"\n")
    
    minimum, count, j = golden(l, r)
    print("golden ratio results:",
          "\nx value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\niterations: ", j, "\n")

    minimum, count, j = newton(5)
    print("newton method results:",
          "\nx value: ", minimum,
          "\nfunction was called: ", count, " times",
          "\niterations: ", j)

if __name__ == "__main__":
    main()