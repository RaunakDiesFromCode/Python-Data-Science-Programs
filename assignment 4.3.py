import random

my_list = [1, 2, 3, 4, 5]

# a. Get a randomly shuffled version of the list
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# b. Get a random element from the list
random_element = random.choice(my_list)
print(f"Random element from the list: {random_element}")
