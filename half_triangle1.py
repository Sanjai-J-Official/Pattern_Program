n=13
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n or i==1:
            print('*',end=" ")
        else:
            print(" ",end=' ')
    print()