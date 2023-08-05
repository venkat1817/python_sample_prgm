# #WAp to fetch all vowels in a string?
# name=input("enter a name:")
# def vowels(name):
#     list =[]
#     for i in name:
#         if i in "aeiou":
#             list.append(i)
#             print(list)
# vowels(name)


# #wap to fetch all words which start with vowels ?
# name="venkat is good boy"
# name=name.split()
# def vowels(name):
#     list =[]
#     for i in name:
#         if i[0] in "aeiou":
#             list.append(i)
#             print(list)
# vowels(name)



#wap to fetch all word which contains "a" characters two are more then two times?
name="i am venkataramireddy"
name=name.split()
def vowels(name):
    list =[]
    for i in name:
        if i.count('a')>=2:
            list.append(i)
    print(list)
vowels(name)