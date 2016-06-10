# Item 3 - Know the Differences Between bytes, str, and unicode


def to_string(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode()
    else:
        value = bytes_or_str
    return value

values = "0x001"
print(to_string(values))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode()
    else:
        value = bytes_or_str
    return value

print(to_bytes(values))


with open("C:\\Users\John\PycharmProjects\Daily Challenge\Challenge_0_guide"
          "\Challenge Number to Name.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line)


with open("C:\\Users\John\PycharmProjects\Daily Challenge\Challenge_0_guide"
          "\Challenge Number to Name.txt", "rb") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
