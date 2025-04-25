n=int(input("Enter the no.of Rows:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==5:
            print("/",end=' ')
        else:
            print("5",end=' ')
    print()