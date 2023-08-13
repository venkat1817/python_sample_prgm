def palindram():
    return s==s[::-1]
s="malayalam"
ans=palindram()
if ans:
    print("yes")

else:
    print("no")