n=int(input("Enter no.of rows:"))
outer=input("Enter outer string:")

for i in range(1,n+1):
    for j in range(1,n+1):
        if  i==j  or  j==(n//2)+1 or i==(n//2)+1 or i+j==n+1:
            print(outer,end=' ')
        else:
            print(" ",end=' ')
    print()
    