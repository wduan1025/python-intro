def show_personal_info(name, age, gender="female", *traveled_to, **additional_info):
    print("name: {name}".format(name=name))
    print("age: {age}".format(age=age))
    print("gender: {gender}".format(gender=gender))
    if len(traveled_to) > 0:
        print(traveled_to)
    if len(additional_info) > 0:
        print(additional_info)
    return 0

print("Argument set 1")
show_personal_info("Alice", 22)
print("\nArgument set 2")
show_personal_info("Adam", 22, "male")
print("\nArgument set 2")
show_personal_info("Adam", "male")
print("\nArgument set 3")
show_personal_info("Charles", 33, "male", "New York", "San Francsco", home="Seattle", martial_status="single")
print("\nArgument set 4")
show_personal_info("Charles", 33, "New York", "San Francsco", home="Seattle", martial_status="single")

def show_personal_info1(*additional_info, name):
    print(additional_info)
    print(name)

print("Calling show_personal_info1, must pass name as a keyword argument")
show_personal_info1(name=1)
