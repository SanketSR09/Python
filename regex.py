import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern1= r'^https?://(?:www\.)?[\w.-]+(?:\.[a-zA-Z]{2,})+[\w\-.?=/]*$'
    return re.match(pattern, email) is not None

# Get email input from the user
email_input = input("Enter an email address: ")

# Check if the email is valid
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")

