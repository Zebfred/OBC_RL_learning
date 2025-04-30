import os
import pwd

def get_username():
  """Detects and returns the current Linux username."""
  return pwd.getpwuid(os.getuid())[0]

if __name__ == "__main__":
  username = get_username()
  print(username)