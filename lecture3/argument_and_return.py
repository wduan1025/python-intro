import time

def show_current_time():
    print(time.time())

def get_current_time():
    return time.time()

def set_guest_list(guest_list):
    guest_list.append("Jason")

def get_possibly_updated_guest_list(guest_list):
    return guest_list + ["Peter"]

print("Calling show_current_time")
show_current_time()
print("Calling  get_curreent_time")
current_time = get_current_time()
print("Current time is ", current_time)
print("Calling set_guest_list")
original_guest_list=["Alice", "Bob"]
print("Original guest_list is ", original_guest_list)
set_guest_list(original_guest_list)
print("Original guest list after calling set_guest_list is ", original_guest_list)
print("Calling get_possibly_updated_guest_list")
possible_list=get_possibly_updated_guest_list(original_guest_list)
print("Original guest list after calling get_possibly_updated_guest_list is ", original_guest_list)
print("Possible guest list is ", possible_list)
