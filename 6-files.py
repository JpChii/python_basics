# Working with file objects
# To access a file object
f = open("test.txt", "r") # The efficent way to interact with files is to use context manager
print(f.name)
# once a file is opened it has to be closes
f.close()

# By doing above methods and if we miss to close the opened file explicitly
# It will lead to leaks and number of open file descriptors
# To avoid this we can use with open context manager,

# File is open only inside the with context and it's automaically closed
with open("test.txt", "r") as f:
    pass

# print(f.read()) # This'll fail with ValueError due to f is closed within context

# Read contents of a file
with open("test.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)

# The above is good for small file but what about large files... we'll run out of memory
# Option 1
with open("test.txt", "r") as f:
    f_contents = f.readlines()
    print(f_contents)

# Option 2
# f.readline() prints line1, line2, line3 and so on
with open("test.txt", "r") as f:
    f_contents = f.readline()
    print(f_contents, end="")
    f_contents = f.readline()
    print(f_contents, end="")

# Option 3
# For loop, with this loop we're not loading entire contets of file in a single go
with open("test.txt", "r") as f:
    for line in f:
        print(line, end="")

# Option 4
# read() specific number of characters, then the next set of characters and so on. 
# At EOF print returns empty file as there's no content left.
with open("test.txt", "r") as f:
    f_contents = f.read(100)
    print(f_contents, end="")

    f_contents = f.read(100)
    print(f_contents, end="")

# Option 5, instead of hardcoding use a loop to read contents in chunks(number of characters) until EOF
with open("test.txt", "r") as f:
    # Read 10 characters at a time
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)

# Get the current position using f.tell()
with open("test.txt", "r") as f:
    # Read 10 characters at a time
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print("\n")
    print(f.tell())

# use seek to set the position in the file
# Print first 10 character go back to position 0
with open("test.txt", "r") as f:
    # Read 10 characters at a time
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    print("\n")
    print(f.tell())
    print("Reset position to 0")
    f.seek(0)
    print(f.tell())
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
    print("\n")
    print(f.tell())

# Writing to a file, set mode to w. In this mode if a file does not exists it'll create a file. 
# If it exists it overwrites the existing contents.
with open("test2.txt", "w") as f:
    f.write("test")

# We can use seek() set position to write as well.

# To read from one file and write to another file we can use nested context managers
with open("source_file.txt", "r") as rf:
    with open("target_file.txt", "wb") as wf:
        size_to_read = 10
        f_contents = rf.read(size_to_read)

        while f_contents > 0:
            wf.write(f_contents)
            f_contents = rf.read(size_to_read)
# To do the same with image files or other file types use rb and wb read and write in binary mode