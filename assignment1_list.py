# Assignment 1
# WAP to implement option of various operations if list
# # Take integer input from user
# # Print list
# # View 1st to 4th element
# # Modify the list in a particular location
# # Add element to the list
# # Remove element from list
# # Sort element of the list 
# # Reverse the list
# # Concatinate 2 list
# # Print every 4th element of the list
# # find the max and min value of the list


li = []
n = int(input("\nEnter the number of elements to input: "))
for _ in range(n):
    li.append(int(input("Enter a number: ")))

print("\nCurrent list:", li)

print("\n1st to 4th elements:", li[:4])

index = int(input("\nEnter the index to modify (0 to {}): ".format(len(li) - 1)))
if 0 <= index < len(li):
    new_value = int(input("Enter the new value: "))
    li[index] = new_value
else:
    print("Invalid index!")

new_element = int(input("\nEnter a new element to add to the list: "))
li.append(new_element)

remove_element = int(input("\nEnter an element to remove from the list: "))
if remove_element in li:
    li.remove(remove_element)
else:
    print(f"{remove_element} not found in the list.")

li.sort()
print("\nFinal sorted list:", li)

li.reverse()
print("\nFinal reversed list:", li)

concat_list = []
concat_len = int(input("\nEnter the number of elements to concatenate: "))
for _ in range(concat_len):
    concat_list.append(int(input("Enter a number to add to the new list: ")))

li.extend(concat_list)

print("Final modified list:", li)

# Print every 4th element of the list
print("\nEvery 4th element of the list:", li[3::4])

# Find the max and min values of the list
max_value = max(li)
min_value = min(li)

print("\nMaximum value in the list:", max_value)
print("\nMinimum value in the list:", min_value)