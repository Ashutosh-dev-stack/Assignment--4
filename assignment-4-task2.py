# Step 1: Create or open the file in write mode
file = open("output.txt", "w")

# Step 2: Write user input to the file
a = input("Enter the text to write to the file: ")
file.write(a + '\n')
print("Data successfully written to output.txt.")

file.close()

# Step 3: Reopen the file in append mode
file = open("output.txt", "a")
b = input("Enter the additional text to append to the file: ")
file.write(b + '\n')
print("Data successfully appended.")
file.close()

# Step 4: Reopen in read mode to display final content
file = open("output.txt", "r")
print("Final content of output.txt:")
print(file.read())
file.close()
