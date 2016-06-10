# Item 6 - Avoid Using start, end, and stride in a Single Slice

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)

w = 'ख़ग़'
x = w.encode('utf-8')
y = x[::-1]
# Throws UnicodeDecodeError...
# z = y.decode('utf-8')

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])

print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])

b = a[::2]
c = b[1:-1]
print(b)
print(c)
