students = []
while True : 
    print ("---------STUDENT MANAGEMENT SYSTEM-----------")
    print ("1. add student ")
    print ("2. veiw student ")
    print ("3. search student ")
    print ("4. delete student ")
    print ("5. exit ")
    choise = input ("enter ur choice (1-5) : ")
    if choise =='1':
     name=input ("Enter students name : ")
    marks = int (input("enter students marks : ") )
    student = {"name" : name , "marks" : marks }
    students.append(student)
    print ("student added successfully")
    elif choise == '2' 
