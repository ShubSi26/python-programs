def diagonalDifference(arr):
    r=0
    c=0
    sm=0
    while r<len(arr) and c<len(arr):
        sm+=arr[r][c]
        r+=1
        c+=1
    r=0
    c=len(arr)-1
    som=0
    while r<len(arr) and c>=0:
        som+=arr[r][c]
        r+=1
        c-=1
    return abs(sm-som)