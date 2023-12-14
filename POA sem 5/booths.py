def twoscomplement(num):
    
    onescomp = ""
    for i in num:
        if i == "0":
            onescomp += "1"
        else:
            onescomp += "0"

    return bin(int(onescomp,2)+int("1",2)).replace('0b',"")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

binnum1=bin(abs(num1)).replace('0b',"")
binnum2=bin(abs(num2)).replace('0b',"")

if(len(binnum1)>=len(binnum2)):
    maxlen=len(binnum1)
else:
    maxlen=len(binnum2)

maxlen+=1

binnum1=binnum1.zfill(maxlen)
binnum2=binnum2.zfill(maxlen)

if num1<0:
    binnum1=twoscomplement(binnum1)

if num2<0:
    binnum2=twoscomplement(binnum2)

bincompnum1=twoscomplement(binnum1)
bincompnum1=bincompnum1.zfill(maxlen)

print(binnum1)
print(binnum2)
print(bincompnum1)

count=maxlen
m=binnum1
q=binnum2
minusm=bincompnum1
q1='0'
a= "0"
a=a.zfill(maxlen)

rightshift=""
while count>0:
    if q[maxlen-1]=="0" and q1=="1":
        a=bin(int(a,2)+int(m,2)).replace("0b","")
        if(len(a)>maxlen):
            a=a[1:]
        a=a.zfill(maxlen)

    if q[maxlen-1]=="1" and q1=="0":
        a=bin(int(a,2)+int(minusm,2)).replace("0b","")
        if(len(a)>maxlen):
            a=a[1:]
        a=a.zfill(maxlen)

    merged=a+q+q1
    rightshift=merged[0]


    for i in range(len(merged)-1):
        rightshift+=merged[i]

    a=rightshift[:maxlen]
    q=rightshift[maxlen:maxlen*2]
    q1=rightshift[-1]
    count-=1

ans=a+q
minus=False

if ans[0] == "1":
    ans=twoscomplement(ans)
    minus=True

print(ans)
if minus:
    print(int(ans,2)*-1)
else:
    print(int(ans,2))

