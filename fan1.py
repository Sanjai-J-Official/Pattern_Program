n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<(n//2)+1 and j<(n//2)+1 and i<j:
            print(" " , end=' ')
        elif i<(n//2)+1 and j>(n//2)+1 and i+j>(n+1) :
            print(" ",end=' ')
        elif i>(n//2)+1 and j>(n//2)+1 and i>j :
            print(" ",end=' ')
        elif i>(n//2)+1 and j<(n//2)+1 and i+j<(n+1) :
            print(" ",end=' ')
        else:
            print("o",end=' ')
        
    print()