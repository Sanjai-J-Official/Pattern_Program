n=int(input("Enter no.of rows:"))
outer=input("Enter outer string:")
inner=input("Enter inter string:")
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==5 or j==5:
            print(outer,end=' ')
        else:
            print(inner,end=' ')
    print()
    