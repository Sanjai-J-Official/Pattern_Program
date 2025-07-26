inp=5

val=inp  
row1=1
for i in range(1,6):
  rows=5-i+1 #i=4==2 , 

  for j in range(1,6):
    rowval=row1+val
    if i>j or i==j:
      if i==j:
        print(i,  end=" ")
      else:
        if j==1:
          
          print(rowval,end=" ")
          row1+=val
          val-=1
        else:
          rowss=row1-rows
          
          print(rowss,end =" ")
          rows+=1
          
         
          
          
         
         
         
        
  print()  
