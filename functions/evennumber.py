#wap to write fetch all even numbers:
list=[10,2,3,4,5,6,7]
def allevennumbers(list1):
    list2 = []
    for i in list1:
        if i%2==0:
            list2.append(i)
            print(list2)
allevennumbers(list)


#wap to print odd and even numbers in given list?
list=[10,2,3,4,5,6,7]
def evenodd(list1):
    list2 = []
    list3=[]
    for i in list1:
        if i%2==0:
            list2.append(i)
            print(list2)
        else:
            list3.append(i)
        print(list3)
evenodd(list)


