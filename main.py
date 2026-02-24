def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

text = read_file("input.txt")
print("=== Text original ===")
print(text)
