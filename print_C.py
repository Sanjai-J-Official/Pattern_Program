n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 and j==1) or (i==n and j==1) or (i==1 and j==n) or (i==n and j==n):
            print(" ", end=' ')
        elif  i==1 or j==1 or i==n :
            print('*',end=" ")
        else:
            print(" ",end=' ')
    print()