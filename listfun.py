li = []

for i in range(4):
    li.append(int(input("Enter a number: ")))

print("List before removal:", li)

remove = int(input("Enter number to remove: "))

if remove in li:
    li.remove(remove)
    print("Updated list:", li)
else:
    print("Nothing to remove. The number was not found in the list.")
