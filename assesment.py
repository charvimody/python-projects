print ("___ouestion 1 ___")
name=("Charvi")
age=(12)
print ("Name :",name)
print ("Age : ",age)
print ("--------------------------------")
print ("___ouestion 2 ___")
number1=int(input("enter the first number :"))
number2=int(input("enter the second number :"))
add=number1+number2
print ("Sum = ",add)
print ("--------------------------------")
print ("___ouestion 3 ___")
number3=int(input("enter a number :"))
if number3%2==0:
    print ("it is a even number ")
else:
    print ("it is an odd number ")
print ("--------------------------------")
print ("___ouestion 4 ___")
number4=int(input("enter the first number :"))
number5=int(input("enter the second number :"))
if number4>number5:
    print ("largest number is : ",number4)
else:
    print ("largest number is : ",number5)
print ("--------------------------------")
print ("___ouestion 5 ___")
for i in range (1,11):
    print (i )
print ("--------------------------------")
print ("___ouestion 6 ___")
number6=int(input("enter a number :"))
for i in range (1,11 ):
      print(number6, "x", i, "=", number6 * i)
print ("--------------------------------")
print ("___ouestion 7 ___")
sum = 0
for i in range(1, 101):
    sum = sum + i
print("Sum =", sum)
print ("--------------------------------")
print ("___ouestion 8 ___")
def square(num):
    return num * num
number = int(input("Enter a number: "))
print("Square =", square(number))
print ("--------------------------------")
print ("___ouestion 9 ___")
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1
print("Number of vowels:", count)
print ("--------------------------------")
print ("___ouestion 10 ___")

print ("--------------------------------")
print ("_____ PROGRAM COMPLETE _____")