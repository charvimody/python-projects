print ("this is while loop")
count = 0
while (count < 9 ):
    print ('the count is :', count)
    count = count +1
print ("goodbye")
print ("-------------------------")
print ("this is infinite loop ")
var=1
while var == 1: 
    num=input ("enter ur name : ")
    print ("u entered :",num)
print ("goodbye")
print ("to find minimum and maximum numbers")
lst=[]
num1=int (input("how namy numbers :") )
for n in range (num1) :
    numbers = int (input ("enter number : "))
    lst.append (numbers) 
    print (" most maximum element in the number is :", max (lst)," most minimum element in the number is :",min(lst) )
    