import os 
import pwd

# Method 1: Using os.path.expanduser()
user = os.environ.get('USER')
user_path = os.path.join("/home", user, "Documents", "my_file.txt")
print(user)
print(user_path)


username = os.path.expanduser("~")
file_path = os.path.join(username, "Documents", "my_file.txt")
print(file_path)
print(username)

# Method 2: Using pwd and os
username = pwd.getpwuid(os.getuid())[0]
file_path = os.path.join("/home", username, "Documents", "my_file.txt")
print(file_path)