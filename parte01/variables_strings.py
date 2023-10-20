### In this case we talk about a variable that type Str

name:str = "Alejandro"  
sur_name:str = "Diaz"
full_name:str = name + " " + sur_name ### When two variable are strings the plus operator concatenate the variables
print(full_name)

print(f"Data type of the variable name is {type(name)}, sur name is {type(sur_name)} and full name is {type(full_name)}")


### Mechanics of concat int and str.

age:int = 24

name_age = name + " " + sur_name + " " + str(age) + " Years old."

print(name_age)