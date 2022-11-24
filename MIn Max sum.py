def miniMaxSum(arr):
    l=[]
    for a in range(len(arr)):
        o=list(arr)
        o.pop(a)
        l.append(sum(o))
    print(min(l),max(l))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)