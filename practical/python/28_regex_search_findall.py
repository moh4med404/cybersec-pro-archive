import re  # Import the regular expressions module

# -------------------------------
# Example 1: Using re.search()
# -------------------------------

# A sample string with a price
text1 = "The price is $45"

# Search for the first occurrence of a dollar sign followed by digits
# Pattern explanation:
# \$   => Escaped dollar sign
# \d+  => One or more digits
match = re.search(r'\$\d+', text1)

print("Example 1: re.search()")
if match:
    # If a match is found, print the matched text
    print("Found match:", match.group())  # Output: $45
else:
    # If no match is found
    print("No match found.")


# -------------------------------
# Example 2: Using re.findall()
# -------------------------------

# A sample string with multiple phone numbers
text2 = "My phone numbers are 123-456-7890 and 987-654-3210"

# Find all phone numbers in the format xxx-xxx-xxxx
# Pattern explanation:
# \d{3} => Exactly 3 digits
# -     => Hyphen
# \d{4} => Exactly 4 digits
matches = re.findall(r'\d{3}-\d{3}-\d{4}', text2)

print("\nExample 2: re.findall()")
# Print the list of all matches found
print("Found matches:", matches)  # Output: ['123-456-7890', '987-654-3210']
