n=13
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==n-1 and j==n) or (i==n-1 and j==n-2) or( i==n-2 and j==n-1)or (j==n-1 and i==n) or (i==1 and j==1) or (i==1 and j==n-1) or (i==n-1 and j==1)or (i==n and j==1) or (j==n and i==1) :
            print(" ", end=' ')
        elif i==1 or j==1 or i==n-1 or j==n-1 or (i==j and i>=(n//2)+1):
            print("*", end=" ")
        
        else:
            print(" ",end=' ')
    print()