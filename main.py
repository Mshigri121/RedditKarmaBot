import requests

while True:
    try:
        user = input("Enter first reddit username: ")
        print("Reddit username 1 is: " + user)
        staticuser = "glucosegains"
        user_url = f"https://old.reddit.com/user/{user}.json"
        user_dict = requests.get(user_url, headers={'User-agent': 'm0'}).json()
        upvote = user_dict["data"]["children"][0]["data"]["ups"]
    except KeyError:
        print("Sorry, this user does not exist.")
        continue
    else:
        break

while True:
    try:
        user2 = input("Enter second reddit username: ")
        print("Reddit username 2 is: " + user2)
        staticuser2 = "user2"
        user_url2 = f"https://old.reddit.com/user/{user2}.json"
        user_dict2 = requests.get(user_url2, headers={'User-agent': 'm0'}).json()
        upvote2 = user_dict2["data"]["children"][0]["data"]["ups"]
    except KeyError:
        print("Sorry, this user does not exist.")
        continue
    else:
        break

user_dict = requests.get(user_url, headers = {'User-agent': 'm0'}).json()
user_dict2 = requests.get(user_url2, headers = {'User-agent': 'm0'}).json()

# The code below was used to iterate through the reddit dictionaries to find our specific key-value pairing
#print(user_dict["data"].keys())
#print(dir(user_dict))
# for key in user_dict:
#     print(key, '->', user_dict[key])
# Nested dictionary containing the last post = data -> children -> data -> ups
# for k, v in user_dict.items():
#   print(k)
#   print(v)

# Create a program that gets information about two different users, and then sees whose most recent post received the most karma.
if upvote > upvote2:
    print(user + "'s last post had more upvotes")
    print("Number of upvotes of " + user + " recent post: " + str(upvote))
    diff = upvote - upvote2
    print("Difference of upvotes between user's last post: " + str(diff))
else:
    diff2 = upvote2 - upvote
    print(user2 + "'s last post had more upvotes")
    print("Number of upvotes of " + user2 + " recent post: " + str(upvote2))
    print("Difference of upvotes between user's last post: " + str(diff2))
# The program should then print out which user received more karma, and what the difference was.
