x = 10
y = 10.5
z = "hello!"

print(type(x))
print(x)
print("                ")
print(type(y))
print(y)
print("                ")
print(type(z))
print(z)
print("                ")

x = x*y
print(x)
print(type(x)) #here the priority gives to float value in every operator the priority goes to float
#this is called implicit type of conversion

#scond the explicit type conversion
print("                ")
age = input("what is your age ? ")
print(type(age)) #the output is class "str" So in next step we can change this into int class
print("                ")
age = int(age)
print(age, type(int(age)))  # so here the class of str change into <class 'int'>



