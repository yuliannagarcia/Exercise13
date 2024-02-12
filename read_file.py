# Open the "pelican.txt" file in read mode ("r")
file_handle = open("pelican.txt", "r")

# Read the entire contents of the file into a string
file_contents = file_handle.read()

# Display the type of the returned data and print the contents
print(type(file_contents))
print(file_contents)

# Close the file handle
file_handle.close()

# Read the "pelican.txt" file into a list and output the number of items within the list
file_handle = open("pelican.txt", "r")

# Move the file cursor to the beginning of the file
file_handle.seek(0)

# Read the lines of the file into a list
file_list = file_handle.readlines()

# Print the number of items in the list
print(len(file_list))

# Close the file handle
file_handle.close()

# Use a loop to iterate over and print the contents of the file without including blank lines
file_handle = open("pelican.txt", "r")

# Iterate over each line in the list
for line in file_list:
    # Check if the line is not empty after stripping whitespace
    if line.strip() != "":
        # Print the line after stripping leading and trailing whitespace
        print(line.strip())

# Close the file handle
file_handle.close()
