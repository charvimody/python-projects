count=0
while count <=100:
    print( count )
    count+=1
    if count == 3:
     break
    print ("----------------")
for i in range (0,5):
   if i ==3:
      continue
   print (i)
print ("-----------")
for i in range (1,11) :
   if i ==5:
    continue
   if i ==9 :
      break 
   print (i)