

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.


def find_element(list,match):
    i = 0
    for element in list:
        if element == match:
            return i
        i += 1
    return -1



            # THIS IS ANOTHER WAY
def find_element(list,match):
    i = 0
    while i < len(list):
        if list[i] == match:
            return i
        i += 1
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
