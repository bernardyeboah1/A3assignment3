#final project
#Group Leader : Bernard Yeboah, Student Number: 100861980
#Group Member : Arvin Naresh, 100869436
import sys
student = []

#Title of log in page
def title():
    title = "Admin Login"
    print(title)
    print("-" * len(title))

title()

def mainmenu():

    def title():
        title = "Student Ledger"
        print(title)
        print('-' * len(title))
    title()

    while True:
        try:
            mainmenu = (input("""Please select an option: 
[1]. Add student 
[2]. Display Student Database
[3]. Search Student Details 
[4]. Exit 
: """))
        except ValueError and UnboundLocalError as error:
            print("Perhaps you made a mistake?")
            print(f"You made a mistake here {error}")
            print("Please try again")
            return mainmenu()


        if mainmenu == str(1):
            addstudent()
        elif mainmenu == str(2):
            displaydatabase()
        elif mainmenu == str(3):
            searchstudentdetails()
        else:
            if mainmenu == str(4):
                print("Goodbye! ")
                sys.exit()

def addstudent():

    newStudent = {
        "Student Number": input("Please enter your student number: "),
        "First Name": input("Please enter your first name: "),
        "Middle Name": input("Please enter your middle name: "),
        "Last Name" : input("Please enter your last name :"),
        "dob" : input("Please enter your date of birth: "),
        "gender" : input("Please enter your gender - m/f: "),
        "department" : input("Please enter your department :  "),
        "email" : input("Please enter your email address: "),
        "emergency contact" : input("Please enter your emergency contact details: "),
        "courses opted" : input("Please enter your opted courses opted: "),
        "Fee Information" : input("Please enter your fee information: "),
        "Awards & Financial Aid" : input("Please enter information on awards and financial aid: "),
        "Final grades": input("Please enter information on final grades: ")
    }

    student.append(newStudent)



    def save():
        save = input("Would you like to save this student? Y/N: ")
        addMoreStudents = input("Would you like to add more students? Y/N : ")
        if addMoreStudents == 'y':
            addstudent()
        else:
            if addMoreStudents ==  'n':
                print("\n")
                for keys, values in newStudent.items():
                    print(f"{keys.capitalize()} : {values}")
                print("\n")

    save()






def displaydatabase():
    print('\n')
    if student == []:
        title = "Student Database"
        print(title)
        print("-" * len(title))

        print("No Data Available!\n")


        choice = (input("""Enter your choice:
[1]. Main Menu
[2]. Exit
: """))

        if choice == "1":
            mainmenu()

        else:
            if choice == "2":
                sys.exit("Goodbye!")

    else:
        print(student,'\n')



def searchstudentdetails():
    pass


def usernamepass():
    #username
    u = "Admin"
    #password
    p = "password"

    username = input("please enter username : ")
    password = input("please enter password : ")
    print("\n")


#if user enters incorrect username
    if username != u:
        print("Incorrect username!")
        print("Please try again...")
        return usernamepass()

#if user enters incorrect password
    elif password != p:
        print("Incorrect password!")
        print("Please try again...")
        return usernamepass()

#if user enters incorrect username and password
    elif username != u and password != p:
        print("Incorrect username and password! :")
        print("Please try again!: ")
        return usernamepass()

    else:
        if username == u and password == p:
            mainmenu()

usernamepass()
