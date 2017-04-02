
print "\nProject Euler - Problem 1"

print "\nMultiples of 3 and 5\n"

print "If we list all the natural numbers below 10"
print "that are multiples of 3 or 5, we get 3, 5, 6 and 9."
print "The sum of these multiples is 23."

print "\nFind the sum of all the multiples of 3 or 5"
print "below 1000.\n"

def multiples_three_n_five():
    sum = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum

print multiples_three_n_five()
