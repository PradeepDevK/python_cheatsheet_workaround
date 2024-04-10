my_list = [1, 0, 2, 0, 'hello', '', []]
print(list(filter(bool, my_list)))

# output will be [1, 2, 'hello']
# The filter() function takes two arguments: a function and an iterable. It filters out elements from the iterable for which the function returns True.
# In this case, the function passed to filter() is bool.
# The bool() function in Python returns False for empty values such as 0, '', [], and None, and True for all other values.
# The filter(bool, my_list) call filters out elements from my_list for which bool(element) is False.
# After filtering, the resulting list contains only elements that are considered True by the bool() function.