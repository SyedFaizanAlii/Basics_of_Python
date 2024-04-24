# in this chapter we disccuss about if else or elif conditions 

print("We are very GrateFull to Chossing our School!")
name = input("Please enter student Name : ")
print("Hello!", name, )
student_age =input("What is the age? ")
student_age = int(student_age)
reuired_age_school = 5
if student_age == reuired_age_school :
    print("Congratulation you can Enroll for School.")
elif student_age < reuired_age_school:
    print("Sorry the age of ",name, "is too short to Enroll in our School!")
elif student_age >= 18 :
    print(name, "Your are too old for our School , Please Contact to Higher Schools Administration")
else :
    print("Congratulation you can Enroll for School.")
