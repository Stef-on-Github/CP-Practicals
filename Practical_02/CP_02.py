user_string = input("Enter a Proper String / Sentence:- ")

def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def count_character(s, char):
    return s.count(char)

def find_substring(s, substring):
    return s.find(substring)  # Returns index of substring or -1 if not found

def is_alpha(s):
    return s.isalpha()

def is_digit(s):
    return s.isdigit()

print("\nChoose an operation:")
print("1. Reverse the string")
print("2. Convert to uppercase")
print("3. Convert to lowercase")
print("4. Count occurrences of a character")
print("5. Find the index of a substring")
print("6. Check if the string contains only alphabetic characters")
print("7. Check if the string contains only digits")

# Get user choice
choice = int(input("Enter the number of your choice: "))

if choice == 1:
    print("Reversed string:", reverse_string(user_string))

elif choice == 2:
    print("Uppercase string:", to_uppercase(user_string))

elif choice == 3:
    print("Lowercase string:", to_lowercase(user_string))

elif choice == 4:
    char = input("Enter the character to count: ")
    print(f"Occurrences of '{char}':", count_character(user_string, char))

elif choice == 5:
    substring = input("Enter the substring to find: ")
    index = find_substring(user_string, substring)
    if index != -1:
        print(f"Substring '{substring}' found at index {index}.")
    else:
        print(f"Substring '{substring}' not found.")

elif choice == 6:
    if is_alpha(user_string):
        print("The string contains only alphabetic characters.")
    else:
        print("The string contains non-alphabetic characters.")

elif choice == 7:
    if is_digit(user_string):
        print("The string contains only digits.")
    else:
        print("The string contains non-digit characters.")

else:
    print("Invalid choice. Please select a number between 1 and 7.")
