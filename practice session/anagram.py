def anagram(str1, str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()

    if sorted(str1)==sorted(str2):
        return True
    
str1=input("enter a string1  ")
str2=input("enter a string2  ")

if anagram(str1,str2):
    print(f"its anagram ")
else:
    print("not anagram")


"""
Logic:
Definition: Two strings are anagrams if they contain the same characters with the same frequency, but the order of characters may differ.
Steps:
First, remove any spaces and ensure both strings are in the same case (e.g., lowercase) for uniformity.
Then, sort both strings alphabetically and compare them. If they are identical, the strings are anagrams.
Alternatively, we can use a frequency count (e.g., collections.Counter) to compare the character counts in both strings.

Explanation of Code:
Remove spaces and case sensitivity: This ensures words like "Listen" and "Silent" (with uppercase) are treated as valid anagrams.
Sorting: The sorted() function sorts the characters of both strings in ascending order. If the sorted versions are identical, they are anagrams.
Comparison: The if condition compares the sorted strings.
"""