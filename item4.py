# Item 4 - Write Helper Functions Instead of Complex Expressions


from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))

print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

# For query string 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)

red = int(my_values.get('red', [''])[0] or 0)

red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

# Helper Function


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found)
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')
