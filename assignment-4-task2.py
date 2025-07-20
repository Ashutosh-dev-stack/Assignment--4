file = open("output.txt", "w")

a = input("Enter the text to write to the file: ")
file.write(a + '\n')
print("Data successfully written to output.txt.")

file.close()

file = open("output.txt", "a")
b = input("Enter the additional text to append to the file: ")
file.write(b + '\n')
print("Data successfully appended.")
file.close()

file = open("output.txt", "r")
print("Final content of output.txt:")
print(file.read())
file.close()
