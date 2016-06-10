# Item 5 - Know How to Slice Sequences


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])

assert a[:5] == a[0:5]

assert a[5:] == a[5:len(a)]

# a[:]      ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# a[:5]     ['a', 'b', 'c', 'd', 'e']
# a[:-1]    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# a[4:]                         ['e', 'f', 'g', 'h']
# a[-3:]                             ['f', 'g', 'h']
# a[2:5]              ['c', 'd', 'e']
# a[2:-1]             ['c', 'd', 'e', 'f', 'g']
# a[-3:-1]                           ['f', 'g']

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

# a[20] -- Throws IndexError

b = a[4:]
print('Before:    ', b)
b[1] = 99
print('After:     ', b)
print('No change: ', a)

print('Before: ', a)
a[2:7] = [99, 22, 14]
print('After:  ', a)

b = a[:]
assert b == a and b is not a

b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b
print('After ', a)
