"""Basket ball """
shot=int(input())#no. shots
a=int(input())#size of sub_array
d=list(map(int,input().split()))
m=0
for i in range(0,len(d)-a+1):
    t=d[i:i+a]
    k=1
    s=0
    for j in t:
        s+=(j*k)
        k+=1
    if(s>m):
        m=s
print(m)