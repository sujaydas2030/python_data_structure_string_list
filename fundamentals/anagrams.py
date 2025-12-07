"""
Checks if two strings are anagrams (ignoring spaces and case).
"""
#function ‘are_anagrams(str1, str2)’
# Taking input
str1 = input()
str2 = input()

def are_anagrams(str1, str2):
    # Write your code here
    str1_list=list(str1.replace(" ","").lower())
    str2_list=list(str2.replace(" ","").lower())
    str1_list.sort()
    str2_list.sort()
    if str1_list==str2_list:
      return True
    else:
      return False

# Print the result
print(are_anagrams(str1, str2))
