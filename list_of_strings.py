

p = ['H', 'e', 'l', 'l', 'o']
print p

p[0] = 'Y'
print p

p[4] = '!'
print p



# Extra example of using a list.

spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1
print agent[2]
