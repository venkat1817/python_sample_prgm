#Wap to find the square of the every number in the list?
list=[2,3,4,5,6,7,8]
def square(list):
    list2=[]
    for i in list:
        x=i**2
        list2.append(x)
        print(list2)
square(list)
