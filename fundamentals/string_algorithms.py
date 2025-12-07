"""
Checks whether the given string is a palindrome.
Ignores spaces, punctuation, and case.
"""
#whether a given string is a palindrome
s=input()
def is_palindrome(s):
  s_list=s.lower().split()
    # Write your code here
  new_s=""
  for word in s_list: # Outer loop iterates through words
   for char in word: # Inner loop iterates through characters in the word
    if char not in string.punctuation: # Check if the character is NOT punctuation
     new_s += char
  new_s_rev=new_s[::-1]
  if new_s==new_s_rev:
    return True
  else:
    return False
# Print the output
print(is_palindrome(s))
