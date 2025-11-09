# myfeature.py

import logging


def greet_user(name):
    """
    Function to greet the user with their name.
    
    Args:
        name (str): The name of the user.
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the feature."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
    print("Welcome to the feature module!")
    