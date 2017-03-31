# Testing Append
# What value is printed after running this code?

p =[1,2]
q = [3,4]
p.append(q)
print len(p)


# Anser: 3
# This is because a list is being appended but
# it counts as only one element.

# What will happen in this case?

q[1] = 5
print p


# It changes the value of 'p', because the
# object that was created, the third element
# of 'p', is actually a reference to the object
# containing [3,4], which is the same list object
# that 'q' refrences.
# So what we change in 'q' is also changed in 'p'.
