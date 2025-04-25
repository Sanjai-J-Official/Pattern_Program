n=int(input("Enter no.of rows:"))
#outer=input("Enter outer string:")
#inner=input("Enter inter string:")
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n//2)+1:
            print('*',end=' ')
        else:
            print("-",end=' ')
    print()
    