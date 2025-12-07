"""takes a list of integers and returns a new list such that each element at index 'i'
of the new list is the product of all the elements
in the original list except the one at 'i'"""
# Import the literal_eval library to safely evaluate string input as a Python
from ast import literal_eval

# Taking input
n = int(input())
arr = literal_eval(input())

def product_except_self(arr):
    # Write your code here
  product_list=[]
  product=1
  for i in range(len(arr)):
    for j in range(len(arr)):
      if i!=j:
        product*=arr[j]
    product_list.append(product)
    product=1
  return product_list

# Print the output
print(product_except_self(arr))
