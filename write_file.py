# Creating a file handle to open and append to a file called "pelican.txt"
file_handle = open("pelican.txt", "a")

# Appending the first line to the file with a newline character "\n"
file_handle.write("A wonderful bird is the pelican,\n")

# Appending the second line to the file with a newline character "\n"
file_handle.write("His bill holds more than his belican.\n")

# Creating a list of lines
lines = ["He can take in his beak, In ", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]

# Appending the list to the file
file_handle.writelines(lines)

# Close the file handle
file_handle.close()
