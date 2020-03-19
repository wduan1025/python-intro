def show_personal_info(name, age, gender="female"):
    print("name: {name}".format(name=name))
    print("age: {age}".format(age=age))
    print("gender: {gender}".format(gender=gender))
    return 0

print("Argument set 1")
show_personal_info("Alice", 22)
print("\nArgument set 2")
show_personal_info("Adam", 22, "male")
print("\nArgument set 2")
show_personal_info("Adam", "male")
print("\nArgument set 3")
show_personal_info("Adam")
