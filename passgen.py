Pass_len=int(input("Length of the password"))

import string
import random

uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

use_upper = input("Include uppercase letters? (y/n): ").strip().lower()
use_lower = input("Include lowercase letters? (y/n): ").strip().lower()
use_numbers = input("Include numbers? (y/n): ").strip().lower()
use_symbols = input("Include symbols? (y/n): ").strip().lower()

# strip() is used to select only text without any whitespaces
# lower() is used to convert letters into lowecase


character_pool=[]

if use_upper == "y":
    character_pool+=uppercase_letters
if use_lower == "y":
    character_pool+=lowercase_letters
if use_numbers == "y":
    character_pool+=numbers
if use_symbols == "y":
    character_pool+=symbols
    
if not character_pool:
    print("You must select at least one character type!")

# Optionally, exit or ask again

else : 
    password="".join(random.choice(character_pool) for _ in range (Pass_len))
    print("Generated Password",password)
