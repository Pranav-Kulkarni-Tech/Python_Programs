# Example string for demonstration
sample_string = " Hello, World! Welcome to Python programming. "

# 1. capitalize() - Capitalizes the first character of the string
capitalized_string = sample_string.capitalize()
print("1. capitalize():", capitalized_string)

# 2. casefold() - Converts the string to lowercase (more aggressive than lower())
casefolded_string = sample_string.casefold()
print("2. casefold():", casefolded_string)

# 3. center(width) - Centers the string within a given width
centered_string = sample_string.center(50)
print("3. center():", repr(centered_string))

# 4. count(sub) - Counts occurrences of a substring
count_hello = sample_string.count("Hello")
print("4. count():", count_hello)

# 5. encode() - Encodes the string using the specified encoding
encoded_string = sample_string.encode('utf-8')
print("5. encode():", encoded_string)

# 6. endswith(suffix) - Checks if the string ends with the specified suffix
ends_with_python = sample_string.endswith("programming. ")
print("6. endswith():", ends_with_python)

# 7. expandtabs(tabsize) - Expands tabs in the string to the specified number of spaces
tab_string = "Hello\tWorld"
expanded_tabs = tab_string.expandtabs(4)
print("7. expandtabs():", expanded_tabs)

# 8. find(sub) - Finds the first occurrence of a substring
find_world = sample_string.find("World")
print("8. find():", find_world)

# 9. format() - Formats the string using placeholders
formatted_string = "Hello, {}. Welcome to {}.".format("Alice", "Wonderland")
print("9. format():", formatted_string)

# 10. index(sub) - Finds the first occurrence of a substring, raises ValueError if not found
try:
    index_world = sample_string.index("World")
    print("10. index():", index_world)
except ValueError:
    print("10. index(): substring not found")

# 11. isalnum() - Checks if all characters are alphanumeric
is_alnum = sample_string.isalnum()
print("11. isalnum():", is_alnum)

# 12. isalpha() - Checks if all characters are alphabetic
is_alpha = sample_string.isalpha()
print("12. isalpha():", is_alpha)

# 13. isdecimal() - Checks if all characters are decimals
is_decimal = sample_string.isdecimal()
print("13. isdecimal():", is_decimal)

# 14. isdigit() - Checks if all characters are digits
is_digit = sample_string.isdigit()
print("14. isdigit():", is_digit)

# 15. isidentifier() - Checks if the string is a valid identifier
is_identifier = "myVariable".isidentifier()
print("15. isidentifier():", is_identifier)

# 16. islower() - Checks if all characters are lowercase
is_lower = sample_string.islower()
print("16. islower():", is_lower)

# 17. isnumeric() - Checks if all characters are numeric
is_numeric = sample_string.isnumeric()
print("17. isnumeric():", is_numeric)

# 18. isprintable() - Checks if all characters are printable
is_printable = sample_string.isprintable()
print("18. isprintable():", is_printable)

# 19. isspace() - Checks if all characters are whitespace
is_space = "   ".isspace()
print("19. isspace():", is_space)

# 20. istitle() - Checks if the string is titlecased
is_title = sample_string.istitle()
print("20. istitle():", is_title)

# 21. isupper() - Checks if all characters are uppercase
is_upper = sample_string.isupper()
print("21. isupper():", is_upper)

# 22. join(iterable) - Joins elements of an iterable with the string as separator
joined_string = ", ".join(["apple", "banana", "cherry"])
print("22. join():", joined_string)

# 23. ljust(width) - Left-justifies the string within the given width
left_justified = sample_string.ljust(50)
print("23. ljust():", repr(left_justified))

# 24. lower() - Converts all characters to lowercase
lowercase_string = sample_string.lower()
print("24. lower():", lowercase_string)

# 25. lstrip() - Removes leading whitespace
lstripped_string = sample_string.lstrip()
print("25. lstrip():", repr(lstripped_string))

# 26. partition(sep) - Splits the string at the first occurrence of sep
partitioned_string = sample_string.partition("World")
print("26. partition():", partitioned_string)

# 27. replace(old, new) - Replaces occurrences of a substring with another substring
replaced_string = sample_string.replace("World", "Universe")
print("27. replace():", replaced_string)

# 28. rfind(sub) - Finds the last occurrence of a substring
rfind_world = sample_string.rfind("World")
print("28. rfind():", rfind_world)

# 29. rindex(sub) - Finds the last occurrence of a substring, raises ValueError if not found
try:
    rindex_world = sample_string.rindex("World")
    print("29. rindex():", rindex_world)
except ValueError:
    print("29. rindex(): substring not found")

# 30. rjust(width) - Right-justifies the string within the given width
right_justified = sample_string.rjust(50)
print("30. rjust():", repr(right_justified))

# 31. rpartition(sep) - Splits the string at the last occurrence of sep
rpartitioned_string = sample_string.rpartition("World")
print("31. rpartition():", rpartitioned_string)

# 32. rsplit(sep) - Splits the string at the separator from the right
rsplit_string = sample_string.rsplit()
print("32. rsplit():", rsplit_string)

# 33. rstrip() - Removes trailing whitespace
rstripped_string = sample_string.rstrip()
print("33. rstrip():", repr(rstripped_string))

# 34. split(sep) - Splits the string at the separator
split_string = sample_string.split()
print("34. split():", split_string)

# 35. splitlines() - Splits the string at line breaks
multi_line_string = "Hello\nWorld\nWelcome"
split_lines = multi_line_string.splitlines()
print("35. splitlines():", split_lines)

# 36. startswith(prefix) - Checks if the string starts with the specified prefix
starts_with_hello = sample_string.startswith(" Hello")
print("36. startswith():", starts_with_hello)

# 37. strip() - Removes leading and trailing whitespace
stripped_string = sample_string.strip()
print("37. strip():", repr(stripped_string))

# 38. swapcase() - Swaps the case of all characters in the string
swapped_case_string = sample_string.swapcase()
print("38. swapcase():", swapped_case_string)

# 39. title() - Converts the string to title case
title_case_string = sample_string.title()
print("39. title():", title_case_string)

# 40. upper() - Converts all characters to uppercase
uppercase_string = sample_string.upper()
print("40. upper():", uppercase_string)

# 41. zfill(width) - Pads the string with zeros on the left to fill the specified width
zero_filled_string = "42".zfill(5)
print("41. zfill():", zero_filled_string)
