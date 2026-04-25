print ("to find minimum and maximum numbers")
lst=[]
num1=int (input("how namy numbers :") )
for n in range (num1) :
    numbers = int (input ("enter number : "))
    lst.append (numbers) 
    print (" most maximum element in the number is :", max (lst)," most minimum element in the number is :",min(lst) )
    