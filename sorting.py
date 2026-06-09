import numbers
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)
print ("-------------------------------------")
print ("now it is sorting alphabets")
alphabets = input("Enter alphabets separated by spaces: ").split()
alphabets.sort()
print("Ascending:", alphabets)
alphabets.sort(reverse=True)
print("Descending:", alphabets)
