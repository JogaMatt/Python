# 1. Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(int):
    newList=[]
    for x in range(int,-1,-1):
        newList.append(x)
    return newList

print(countdown(5))


# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def receiveNum(list):
    print(list[0])
    return list[1]

print(receiveNum([5,7]))


# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def listMath(list):
    num1 = list[0]
    num2 = len(list)
    sum = num1 + num2
    return sum

print(listMath([10,3,3]))


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from
# the original list that are greater than its 2nd value. Print how many values this is and then return the new list.
#  If the list has less than 2 elements, have the function return False

def notWelcomed(list):
    if len(list) < 2:
        return False
    newList = []
    for val in list:
        if val > list[1]:
            newList.append(val)
    return newList

print(notWelcomed([4,2,5,6,1,7]))


# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def newFunction(num1,num2):
    newList = []
    for x in range(num1):
        newList.append(num2)
    return newList

print(newFunction(8,4))