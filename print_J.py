n=13
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 and i==n) or (i==n and j==(n//2)+1):
            print(" ",end=' ')
        elif i==1 or j==(n//2)+1 or j==1 and i>(n//2)+1 or i==n and j<(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()