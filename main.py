# This Project done by J.Maheswara Moorthy in Chenaai-India

# Seminar Entry Pass System


entryPassDetails = []
noOfParticipantsAllowed = 2
passNo = 1
studentCount = 0
employeeCount = 0
unEmployeeCount = 0

while passNo <= noOfParticipantsAllowed:
    print("Welcome to DSIT Seminar")
    name = input("Name of the Participant                    : ")
    place = input("Place                                      : ")
    category = input("Category (S)tudent/(E)mployee/(U)nEmployee : ")

    print("\n---------------------------------------------------------------")
    print("                     Data Science In Tamil                     ")
    print("                      Anna Salai, Chennai")
    print("                    Seminar on Data Science")
    print("                      E N T R Y   P A S S")
    print("Pass No.: ", passNo)
    print("Name    : ", name)
    print("Place   : ", place)
    print("Category: ", category.title())
    print("-----------------------------------------------------------------\n\n")

    if category.lower() == 'student':
        studentCount += 1
    elif category.lower() == 'employee':
        employeeCount += 1
    elif category.lower() == 'unemployee':
        unEmployeeCount += 1

    passNo += 1


print("---------------------------------------------------------------")
print("                     Data Science In Tamil                     ")
print("                      Anna Salai, Chennai")
print("                    Seminor On Data Science")
print("                           R E P O R T")
print("No of Participants: ", noOfParticipantsAllowed)
print("No of Students    : ", studentCount)
print("No of Employees   : ", employeeCount)
print("No of Un-Employees: ", unEmployeeCount)
print("---------------------------------------------------------------")