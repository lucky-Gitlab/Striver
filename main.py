from Patterns.patterns import *
a = int(input("enter rows number : "))

b = str(input("enter pattern : "))

if b == 'r':
    reactanglePattern(a)
elif b == 'c':
    circlePattern(a)
elif b == 's':
    starPattern(a)
elif b == 't':
    trianglePattern(a)
elif b == 'n':
    numTrianglePattern(a)
elif b == 'u':
    num2TrianglePattern(a)
elif b == "rev":
    revTrianglePattern(a)
elif b == "rN":
    revNumTrianglePattern(a)
elif b == "au":
    arrowUp(a)
elif b == "ad":
    arrowDown(a)
elif b == "di":
    arrowUp(a)
    arrowDown(a)
elif b == "ar":
    arrowRight(a)
elif b == "al":
    arrowLeft(a)


else :
    print("no such ",b ," pattern found")