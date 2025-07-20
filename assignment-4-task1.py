# program for file opening and reading-----

file = open("sample.txt", "r")

# open the file in read mode
for index, line in enumerate(file, start=1):
        print(f"Line {index}: {line.strip()}")
data = file.read()
print(data)



