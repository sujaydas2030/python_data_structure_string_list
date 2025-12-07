#a function ‘is_balanced(s)’ that checks if the parentheses in the given string are balanced
# Taking input
s = input()

def is_balanced(chars):
    # Write your code here
  round_bracket='('
  curly_bracket='{'
  square_bracket='['
  found_brackets=[]
  bracket_closed=False
  for char in chars:
    if char==round_bracket or char==curly_bracket or char==square_bracket:
      found_brackets.append(char)
  closing_bracket_needs=[]
  for bracket in found_brackets:
    if bracket==round_bracket:
      closing_bracket_needs.append(')')
    elif bracket==curly_bracket:
      closing_bracket_needs.append('}')
    elif bracket==square_bracket:
      closing_bracket_needs.append(']')
  print(found_brackets)
  print(closing_bracket_needs)
  if len(found_brackets)!=len(closing_bracket_needs):
    return False
  for char in chars:
    if char == ')': # If it's a closing round bracket
      if not closing_bracket_needs or closing_bracket_needs.pop() != ')':
        return False  # Mismatch or empty stack
    elif char == '}': # If it's a closing curly brace
      if not closing_bracket_needs or closing_bracket_needs.pop() != '}':
        return False  # Mismatch or empty stack
    elif char == ']': # If it's a closing square bracket
      if not closing_bracket_needs or closing_bracket_needs.pop() != ']':
        return False
  return not closing_bracket_needs


# Print the output
print(is_balanced(s))
