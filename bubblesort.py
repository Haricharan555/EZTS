def s(data):
    n=len(data)-1
    for j in range(0,n):
        for i in range(0,n-j):
            if data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i]
