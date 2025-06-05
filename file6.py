def oneoddoccuring(array):
    res = 0
    for element in array:
        res = res ^ element
    return res

arr = []
n = int(input("enter the array size: "))
while(n):
    number = int(input("enter the element: "))
    arr.append(number)
    n -=1
print("oneoddoccuring number is:",oneoddoccuring(arr))