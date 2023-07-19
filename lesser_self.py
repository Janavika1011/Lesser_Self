def lesser_self(arr):
    a=[]
    for i in range(len(arr)):
        count=0
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                count+=1
        a.append(count)
    return a

arr=list(map(int,input("Enter : ").split()))
print(lesser_self(arr))