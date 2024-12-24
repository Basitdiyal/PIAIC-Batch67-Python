fruit_list = ["apple","orange","Apple", "banana"]
user_consent = input("Do you want to sort the list alphabetically? ")
if user_consent== "yes":
    fruit_list.sort()
    print(fruit_list)

longest_fruit_name = max(fruit_list, key=len)
print("Longest Fruit Name",longest_fruit_name)
shortest_fruit_name = min(fruit_list, key=len)
print("Shortest Fruit Name:", shortest_fruit_name)