n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==n and j==1) or (i==n and j==n):
            print(" ",end=' ')
        elif j==1 or j==n or i==n:
            print("*", end=' ')
        
        else:
            print(" ",end=' ')
    print()