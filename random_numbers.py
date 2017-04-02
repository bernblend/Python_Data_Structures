from random import randint


print "\nUse of while loop:\n"

# Create a list of random numbers from 0 to 10.
# The length of the list is 20.
# I want a list with 20 randomly generated numbers.

def random_list():
    count = 0
    random_list = []
    list_length = 17
    while count < list_length:
        random_list.append(randint(0,10))
        count += 1
    return random_list

print random_list()


print "\nUse of for loop:\n"


def random_list():
    count = 0
    random_list = []
    list_length = 15
    for number in range(list_length):
        random_list.append(randint(0,10))
        count += 1
    return random_list

print random_list()
