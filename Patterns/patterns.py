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
def arrowLeft(n):
    for i in range(2*n-1):
        for j in range(n):
            if i<n:
                if j >= n-1-i:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
            else:
                if j>= i-n+1:
                    print("*", end = " ")
                else:
                    print(" ", end = " ")
        print("\n")
def binaryTriangle(n):
    for i in range(n):
        for j in range(i+1):
            if (i +j)%2 == 0:
                print("1",end = " ")
            else:
                print("0", end = " ")
        print("\n")             

def vPattern(n):
    for i in range(n):
        for j in range(2*n):
            if j<=i:
                print("*", end = " ")
            elif j>=2*n-i-1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("\n")
        
def vPatternNum(n):
    for i in range(n):
        for j in range(2*n):
            if j<=i:
                print(j+1, end = " ")
            elif j>=2*n-i-1:
                print(2*n-j, end = " ")
            else:
                print(" ", end = " ")
        print("\n")

def vRevPattern(n):
    for i in range(n):
        for j in range(2*n):
            if j<=n-i:
                print("*", end = " ")
            elif j>n+i:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("\n")

def countingPattern(n):
    a = 1
    for i in range(n):
        for j in range(i+1):
            print(a, end = " ")
            a = a+1
        print("\n")
        
def abcdPattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()

def abcdRevPattern(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j), end =" ")
        print()

def abcdStaticPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i), end = " ")
        print()

def  abcTriangle(n):
    for i in range(n):
        for j  in range(n+i):
            if j>= n-i-1 and j<n :
                print(chr(65+j-(n-i-1)), end = " ")
            elif j>= n:
                print(chr(65-j+(n+i-1)), end = " ")
            else:
                print(" ", end = " ")
        print()
def edcTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+n-1-i+j), end = " ")
        print()