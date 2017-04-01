


# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.


def measure_udacity(list):
    sum = 0
    for letter in list:
        if letter[0] == 'U':
            sum += 1
    return sum



print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2
