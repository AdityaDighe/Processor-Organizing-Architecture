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

maxlen=len(binnum1)

binnum1=binnum1.zfill(maxlen)
binnum2=binnum2.zfill(maxlen+1)

bincompnum2=twoscomplement(binnum2)
bincompnum2=bincompnum2.zfill(maxlen)

count=maxlen
m=binnum2
minusm=bincompnum2
q=binnum1
a="0"
a=a.zfill(maxlen+1)

leftshift=""
while count>0:
    merged=a+q
    leftshift=merged[1:]
    a=leftshift[:maxlen+1]
    a=bin(int(a,2)+int(minusm,2)).replace("0b","")
    if len(a)>maxlen+1:
        a=a[1:]
    a=a.zfill(maxlen+1)

    if a[0] == "0":
        leftshift = a+q[1:]
        leftshift += "1"

    else:
        a=bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a) > maxlen+1:
            a=a[1:]
        a=a.zfill(maxlen)
        leftshift=a+q[1:]
        leftshift+="0"

    a=leftshift[:maxlen+1]
    q = leftshift[maxlen+1:]
    count -=1

if a[0] == "1":
    a = bin(int(a,2)+int(m,2)).replace("0b","")
    if len(a) > maxlen+1:
        a = a[1:]

print("Remainder",int(a,2))
print("Quotient",int(q,2))
