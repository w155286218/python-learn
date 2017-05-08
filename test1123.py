import kmc2

data=[5,3,9,7,1,6]

print("begin:",data)
for m in range(0,len(data)):
    for n in range(1,len(data)-m):
        if data[n-1]>data[n]:
            temp=data[n-1]
            data[n-1]=data[n]
            data[n]=temp
            print data
    print data
print("end:",data)