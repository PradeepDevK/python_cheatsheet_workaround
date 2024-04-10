l1 = ['A']
l1.extend('ABC')
print(l1)

# output will be ['A', 'A', 'B', 'C']
# Initially, l1 is a list containing a single element 'A'.
# The extend() method is called on l1 with the argument 'ABC'.
# The extend() method iterates over the characters in the string 'ABC' and appends each character to the end of the list l1.