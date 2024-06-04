import re

def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

email1 = "example@example.com"
print(is_valid_email(email1))   
print(is_valid_email("jahnavi@gmail.com"))  
print(is_valid_email("vzjhdckd3hgamil.com")) 