def show_personal_info(name, age, gender, **other_info):
    print("name: {name}".format(name=name))
    print("age: {age}".format(age=age))
    print("gender: {gender}".format(gender=gender))
    for k,v in other_info.items():
        print("{k}: {v}".format(k=k, v=v))

show_personal_info("Sam", 23, "male", martial_status="single", city="New York", infected=False)