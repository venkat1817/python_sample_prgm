# This is reversed number in python
num = 123456
num1=(str(num)[::-1])
print(num1)



# This program is used to while loop 
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))





# This program reverse in string
num = "venkat"
num1=(str(num)[::-1])
print(num1)