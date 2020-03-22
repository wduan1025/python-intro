class Dog:
    name = "John"
    friends = {
        "Chrales" : ["John", "Alice", "Bob"],
        "Alice": ["Bob", "Charles"],
        "Iris": ["Bob", "John"]
    }

dog = Dog()
name = "Alice"
# name = "xxx"
friend_idx = 4
try:
    friends_of_friend = dog.friends[name]
    friend_at_index = friends_of_friend[friend_idx]
    print(friend_at_index.friend)
except KeyError:
    print("Friend name not found")
    friend_at_index = None
except IndexError:
    print("Friend's friend list index exceeded")
    friend_at_index = friends_of_friend[0]
except:
    print("Unkown Error")
    friend_at_index = None

print(friend_at_index)
