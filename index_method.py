


p = [0, 1, 2]
print p.index(2)
# OUTPUT: 2    because that is the index where '2' appears in
#              the list.


p = [0, 1, 2, 2, 2]
print p.index(2)
# OUTPUT: 2    because that is the index where '2' appears in
#              the list FIRST.

# NOTE: if '2' were not in the list it would return an error.




print "\nUSING 'in' with a different context "
print "than in the 'for loop'.\n"


print "\n Syntax:    <value> in <list>"

print "English: is '3' in the list?\n"

print "Python:  '3 in p'  "


p = [0, 1, 2]
print 3 in p

print "OUTPUT: False     because '3' is not in the list."
