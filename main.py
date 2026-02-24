import string

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

text = read_file("input.txt")
print("=== Text original ===")
print(text)

text = remove_punctuation(text)
print("=== Fara punctuatie ===")
print(text)def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

text = read_file("input.txt")
print("=== Text original ===")
print(text)
