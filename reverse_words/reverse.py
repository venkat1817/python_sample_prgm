#python is hight level lang:
st1="python is hight level lang"
st2=st1.split()
# print(st2[-1::-1])
print(' '.join(st2[-1::-1]))
#output
# lang level hight is python


# reverse this every word.
st="python is hight level lang"
st1=st.split()
st2=[]
print(st1)
for i in st1:
    st2.append(i[-1::-1])
    st3=' '.join(st2)
    print(st3)

# #output
# nohtyp si thgih level gnal

st1="python is hight level lang"
st=[]
for i in st1:
    if i in 'aeiou':
        st.append(i)
        print(' ',join(st))



st1="python is hight level lang"
st=[]
for i in st1:
    if i not in 'aeiou':
        st.append(i)
        print(' ',join(st))