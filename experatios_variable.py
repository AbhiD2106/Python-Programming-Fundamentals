print(2+4+4+12)
# 2+4+4+12 - this is one expression

a = 5
print(a + 10)
# a is a variable that holds the value 5

b = 20/a
print(b)
# b is a variable that holds the result of 20 divided by the value of a

# string operation

greeting = "Hello, "
name = "abhi"
full_greeting = greeting + name
print(full_greeting)
# greeting and name are string variables, full_greeting concatenates them

ab = 3*name
print(ab)
# ab is a variable that holds the string 'abhi' repeated 3 times

# \  operator example

# \n 
multiline_string = "This is line one.\nThis is line two."
print(multiline_string)

# \t
tabbed_string = "Column1\tColumn2\tColumn3"
print(tabbed_string)

# \  - continuation character
long_string = "This is a very long string that we want to " \
              "continue on the next line for better readability."
print(long_string)


# \\ - backslash character
path = "ssxq\\qw\\new_folder\\file.txt"
print(path)

# string methods

sample_text = "  Hello, World! Welcome to Python programming.  "
print(sample_text.lower())  # Convert to lowercase
print(sample_text.upper())  # Convert to uppercase
print(sample_text.strip())  # Remove leading and trailing whitespace
print(sample_text.replace("World", "Universe"))  # Replace substring
print(sample_text.split(","))  # Split string by comma
print(sample_text.find("Python"))  # Find substring index
print(sample_text.startswith("  Hello"))  # Check if starts with substring
print(sample_text.endswith("programming.  "))  # Check if ends with substring
print(sample_text.count("o"))  # Count occurrences of a character
print(sample_text.index("Welcome"))  # Get index of substring
print(sample_text.capitalize())  # Capitalize first character
print(sample_text.title())  # Title case
print(sample_text.isalpha())  # Check if all characters are alphabetic
print(sample_text.isdigit())  # Check if all characters are digits
print(sample_text.isspace())  # Check if all characters are whitespace
print(sample_text.center(50))  # Center the string within a specified width
