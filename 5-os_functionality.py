# We can use the os module to interact with the underlying operating system
# Import os module
import os
from utils import print_with_new_line
from datetime import datetime

print_with_new_line(f"Attributes and methods available withing os module: {dir(os)}")
print_with_new_line(f"Current working directory: {os.getcwd()}")
os.chdir("../")
print_with_new_line(f"Current directory after switching to previous dir: {os.getcwd()}")
print_with_new_line(f"List contents of current directory: {os.listdir()}")
# To create a single directory mkdir, to created nested directories mkdirs
os.mkdir("level1_dir")
print_with_new_line(f"Directory list after mkdir level1_dir: {os.listdir()}")
os.makedirs("level1_d/level2_d", exist_ok=True) # This will fail with mkdir as level1_d doesn't exist
print_with_new_line(f"Directory list after mkdirs level1_d/level2_d: {os.listdir("level1_d/")}")
# similar to mkdir and makedirs, rmdir and removedirs works
os.rmdir("level1_dir")
print_with_new_line(f"Directory list after rmdir level1_dir: {os.listdir()}")
os.removedirs("level1_d/level2_d")
print_with_new_line(f"Directory list after removedirs level1_d/level2_d: {os.listdir()}")
# Rename os.rename("original_name", "new_name")
if not os.path.exists("dummy_docs"):
    os.rename("dummy_docs.txt", "dummy_docs")
os.rename("dummy_docs", "dummy_docs.txt")
print_with_new_line(f"Directory list after rename of dummy_docs to dummy_docs.txt: {os.listdir()}")
# We can get stats about a file using os.stat(file)
print(f"Stats about a file:\n {os.stat("test.py")}")
print("1. Here st_size is size of the file in bytes")
print("1. st_mtime is the last modified time of file in timestamp format")
print(f"Last modified time in timestamp format: {os.stat('test.py').st_mtime}")
print_with_new_line(f"Last modified time in human readable format: {datetime.fromtimestamp(os.stat('test.py').st_mtime)}")

# Traversing a directory, we can use os.walk(). This returns a (dir_path, dirs, files). This traverses until it reaches 
# the end of the directory tree
print("Traversing a file system from toptodown")
for dirpath, dirnames, filenames in os.walk("."):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
print_with_new_line("")

# Accessing environment variable
print_with_new_line(f"Get HOME environment variable: {os.environ.get('HOME')}")

# Joining paths with os.path.join is preferred over concatenation or formatted string to avoid
# if / is present or avoiding multiple //

print_with_new_line(f"Joining HOME environment variable with text.py: {os.path.join(os.environ.get('HOME'), 'test.txt')}")

# Accesing directory, filename, extension from a path
print("Accesing directory, filename, extension from a path")
dummy_path = "dummy/dummy.txt"
print(f"Dummy path: {dummy_path}")
print(f"Get directory from path: {os.path.dirname(dummy_path)}")
print(f"Get filename from path: {os.path.basename(dummy_path)}")
print(f"Get file extenstion from path: {os.path.splitext(dummy_path)}")
print(f"If the directory exists: {os.path.isdir(os.path.dirname(dummy_path))}")
print(f"If the file exists: {os.path.isfile(os.path.basename(dummy_path))}")
print(f"If the entire path exists: {os.path.exists(dummy_path)}")
print_with_new_line("")
print_with_new_line(f"All methods and attributes with os.path:\n {dir(os.path)}")