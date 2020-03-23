print("Hello, Welcome to Cat Cafe")
# print("Here is a list of our items:")

cafe_list = []

for item in range(len(cafe_list)):
    print(cafe_list[item])

# ask user to pick the items they want
def show_help():
    print("What cafe items would you like?")
    print(
        """
Enter "DONE" to stop adding items.
Enter "HELP" for this help.
Enter "SHOW" to see your current list.
"""
    )


def add_to_list(item):
    cafe_list.append(item)
    print("Added: List has {} items.".format(len(cafe_list)))


def show_list():
    print("Here's your list:")
    for item in cafe_list:
        print(item)


show_help()
while True:
    new_item = raw_input(">")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue

    add_to_list(new_item)

show_list()

# show the list of items the user has picked
