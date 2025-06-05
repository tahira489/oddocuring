def twooddoccuring(arr,size):
    xor= arr[0]
    x = 0
    y = 0
    setbit = 0
    for i in range(1,size):

        xor = xor ^ arr[i]
    setbit = xor & ~(xor-1)
    for i in range(size):
        if(arr[i] & setbit):
            x= x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("twoodd ocurring elements are",x, y)

arr = []
size = int(input("enter the size of the array"))
for i in range(size):
    num = int(input("enter elemnet: "))
    arr.append(num)

twooddoccuring(arr,size)