#WAp to fetch all 3 divisibles  from the given list?
list=[10,20,30,40,65,4,32,15]
def division(list):
    list1 =[]
    for i in list:
        if i%3==0:
            list1.append(i)
            print(list1)
division(list)

#wap to filter all numbers which is even number and divisible by 3.
def filter_even_and_divisible_by_three(numbers):
    list1 = []
    for i in numbers:
        if i % 2 == 0 and i % 3 == 0:
            list1.append(i)
            print(list1)

# Test the function
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20]
filter_even_and_divisible_by_three(list)


    
