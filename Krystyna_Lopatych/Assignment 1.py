name = "Krystyna"
surname = "Lopatych"
#1 Data types:
print("The data type of 'name' is", type(name))
print("The data type of 'surname' is", type(surname)) 
#2 Strings and their operations:
full_name = name + " " + surname
print(full_name)
print(full_name * 4)
print(full_name[0:5])
print(full_name.upper()) 
#3 List
list = list(full_name)
print(list, "The number of elements in a list: ", len(list))
print(list.pop(2), list.pop(4))
print(list)
#4 If/elif/else conditions
i = 0
while i < len(list):
    if list[i] == "t":
        print("Found T!")
    elif list[i] == "c":
        print("Found C!")
    else:
        print("Another:", list[i])
    i += 1
#5 For and While loop
i = 0
for i in range (len(list)):
    print(list[i])
while list:   
    print("Deleting:", list.pop(0))
print("The list is empty")


