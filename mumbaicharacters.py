S='mumbai'
for j in range(6):
    print(S[j],ord(S[j]))
    j=j+1
"""sum"""
for j in range(1,6):
    f=ord(S[j])+ord(S[j-1])
    j=j+1
print('sum of unicode is:=',f)
"""list unicode"""
l=[]
for j in range(6):
    l.append[ord(S[j])]
    j=j+1
print(l)
"""list comparison"""
l=[ord(S[j]) for j in range(6)]
"""map class"""
l=map(ord,S)
print(list(l))
