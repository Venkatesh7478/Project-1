def get_marks(): 
    name=input("Enter Student Name:")
    python_marks=int(input("Enter Python Marks:"))
    java_marks=int(input("Enter Java Marks:"))
    sql=int(input("Enter SQL Marks:"))
    return name,python_marks,java_marks,sql
def calculate_total(python_marks,java_marks,sql):
        Total_Marks=(python_marks+java_marks+sql)
        return Total_Marks
def calculate_average(Total_Marks):
    Average=(Total_Marks/3)
    return Average
def calculate_grade(Average):
    python_marks=int(input("Enter Python Marks:"))
    java_marks=int(input("Enter Java Marks:"))
    sql=int(input("Enter SQL Marks:"))
    Total_Marks=(python_marks+java_marks+sql)
    Average=(Total_Marks/3)
    if Average>90:
        print("GRADE:A")
    elif Average>80:
        print("GRADE:B")
    elif Average>65:
        print("Grade : C")
    elif Average>50:   
        print("GRADE:D")
    else:
        print("GRADE:D")

def menu():
    name,python_marks,java_marks,sql=get_marks()
    while True:
        print("=== STUDENT GRADE CALCULATOR===")
        print("1.Dispaly the subject marks")
        print("2.Calculate the Total_marks:")
        print("3.Calculate the Average Marks: ")
        print("4.Calculate the Grade:")
        print("5. Exit")
        option = int(input("Enter a option:"))
        if option==1:
                print("Enter Student Name:",name)
                print("Enter Python Marks:",python_marks)
                print("Enter Java Marks:",java_marks)
                print("Enter SQL Marks:",sql)
             
        elif option==2:
           Total_Marks=(python_marks+java_marks+sql)
           print("Total_Marks : ",Total_Marks)    
        elif option==3:
         Average=(Total_Marks/3)
         print("Average :",Average)
        elif option==4:
            Total_Marks=(python_marks+java_marks+sql)
            Average=(Total_Marks/3)
            calculate_grade(Average)
        elif option==5:
            print("Exit Successfully")
            print("Thank you")
        
        else:
            print("enter a valid option")
menu()

