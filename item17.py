# Item 17 - Be Defensive When Iterating Over Arguments


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_numbers.txt')
# percentages = normalize(it)
# print(percentages)

print(list(it))
print(list(it))


def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


def normalize_func(get_iter):
    total = sum(get_iter())  # New iterator
    result = []
    for value in get_iter(): # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits('my_numbers.txt'))


class ReadVisits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits('my_numbers.txt')
percentages = normalize(visits)
print(percentages)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)  # No error
visits = ReadVisits('my_numbers.txt')
normalize_defensive(visits)  # No error

it = iter(visits)
normalize_defensive(it)
