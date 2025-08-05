def basicRecussion(n):
    if n <= 0:
        return
    print(n)
    basicRecussion(n+1)

counter = 0
def printName(name):
    print(name)
    global counter 
    counter = counter + 1
    if counter == 5:
        return
    printName(name)

def printNum(num):
    for i in range(num):
        print(i+1)

def printNumR(num):
    if num == 0:
        return
    print(num)
    printNumR(num-1)
