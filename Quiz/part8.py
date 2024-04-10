l1 = [10, 20, 30, 40]
l1[1:3] = 50
print(l1)

# TypeError: can only assign an iterable
# In the line l1[1:3] = 50, you're trying to assign a single value 50 to a slice of l1 from index 1 (inclusive) to index 3 (exclusive). This operation is not valid because the value being assigned (50) does not match the length of the slice.

# with correction
l1[1:3] = [50]
print(l1)

# return [10, 50, 40]