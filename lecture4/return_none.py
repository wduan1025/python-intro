def convert_to_int(s):
    if not s.isnumeric():
        return None
    return int(s)

s = "12223"
converted_number = convert_to_int(s)
if converted_number is not None:
    print("converted number is : ",converted_number)
else:
    print("Wrong input. Plz try again")