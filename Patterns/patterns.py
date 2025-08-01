def reactanglePattern(n):
    """please enter a integer value > 0"""
    for i in range(n):
        for j in range(n):
            print("* ",end="")              

        print("\n")

def starPattern(n):
    """please enter a integer value > 0"""
    for i in range(n):
        for j in range(n):
            print("* ",end="")              

        print("\n")

def circlePattern(n):
    """please enter a integer value > 0"""
    for i in range(n):
        for j in range(n):
            print("* ",end="")              

        print("\n")

def trianglePattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ") 
        print("\n")

def numTrianglePattern(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print("\n")
def num2TrianglePattern(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=" ")
        print("\n")

def revTrianglePattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end = " ")
        print("\n")

def revNumTrianglePattern(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end = " ")
        print("\n")
        
def arrowUp(n):
    for i in range(n):
        for j in range(n+i):
            if j >= n-i-1:
                print("*", end = " ")
            else:
                print(" ",end = " ")
        print("\n")

def arrowDown(n):
    for i in range(n):
        for j in range(2*n-i-1):
            if j>=i:
                print("*",end = " ")
            else:
                print(" ",end = " ")
        print("\n")

def arrowRight(n):
    for i in range(2*n-1):
        if i < n :
            for j in range(i+1):
                print("*", end = " ")
            print("\n")
        else:
            for j in range(2*n-i-1):
                print("*", end = " ")
            print("\n")