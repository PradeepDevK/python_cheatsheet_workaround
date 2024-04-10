s = 'amazing'
print(s.index('a', 2, 2))

# ValueError: substring not found
# This error occurs because the substring 'a' is not found within the specified indices [2, 2), which essentially means the substring cannot exist between the start and end indices provided.

print(s.index('m', 0, 2))
# returns 1