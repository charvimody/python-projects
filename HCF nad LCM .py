def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The H.C.F. is", compute_hcf(num1, num2))
print ("------------------------------")
print ("now we will calculate the LCM")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
greater = max(num1, num2)
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1
print("LCM =", lcm)