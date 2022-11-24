def print_rangoli(size):
    if size==1:
        print("a")
        return
    # your code goes here
    b=(size*2-2)*2+1
    nub=96+size
    crh=chr(nub)
    lt=[]
    for a in range (0,size):
        if a==0:
            print(crh.center(b,"-"))
        else:
            temp=crh
            crh=crh+chr(nub-a)
            crh1=crh+temp[::-1]
            y=("-".join(crh1)).center(b,"-")
            lt.insert(0,y)
            print(y)
    lt.pop(0)
    for z in lt:
        print(z)
    print(chr(nub).center(b,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)