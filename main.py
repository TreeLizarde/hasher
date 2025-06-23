from random import randint

def generate_salt(length=16) -> str:
    """Generates a random salt of specified length."""
    return ''.join(chr(randint(33, 126)) for _ in range(length))

def hash(input: str) -> str:
    """A simple hash function that returns the sum of ASCII values of characters."""
    return hex(sum(ord(char) for char in (input)))

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = generate_salt()
        self.hashed_password = hash(password + self.salt)

    def check_password(self, input_password: str) -> bool:
        """Checks if the provided password matches the stored hashed password."""
        new_hash = hash(input_password + self.salt)
        return new_hash == self.hashed_password

users: dict[str, User] = { }

def register_user(username: str, password: str) -> None:
    """Registers a new user and returns the User object."""
    users[username] = User(username, password)

def check_credentials(username: str, password: str) -> None:
    """Checks if the provided username and password are valid."""
    if username not in users:
        print(f"Username not found.")
    
    user = users[username]

    is_valid = user.check_password(password)
    if is_valid:
        print(f"Login successful.")
    else:
        print(f"Incorrect password.")


register_user("username123", "password123")

check_credentials("username123", "password123")
check_credentials("username123", "wrongpassword")




