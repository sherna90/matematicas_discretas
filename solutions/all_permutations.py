import numpy as np

def all_permutations(arr):
    c=0
    n=len(arr)
    while c<factorial(n):
        p=np.random.permutation(n)
        yield [arr[i] for i in p]
        c+=1

def next_permutation(arr):
    n=len(arr)
    j=n-2
    while arr[j]>arr[j+1]:
        j=j-1
    k=n-1
    while arr[j]>arr[k]:
        k=k-1
    temp=arr[j]
    arr[j]=arr[k]
    arr[k]=temp
    r=n-1
    s=j+1
    while r>s:
        temp=arr[r]
        arr[r]=arr[s]
        arr[s]=temp
        r=r-1
        s=s+1
    return arr
        
def lexicographic_permutation(arr):
    c=0
    arr.sort()
    n=len(arr)
    while c<factorial(n):
        if c==0:
            yield arr
        else:
            yield next_permutation(arr)
        c=c+1
