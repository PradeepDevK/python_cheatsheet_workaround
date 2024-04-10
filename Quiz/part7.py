a = { 'name': 'abc' }
b = a
c = a.copy()
a['name'] = 'xyz'
print(b['name'], c['name'])

# output will 'xyz abc'
# a = {'name': 'abc'}: This line creates a dictionary a with a key 'name' mapped to the value 'abc'.
# b = a: This line assigns the reference of dictionary a to b. Now, b refers to the same dictionary object as a.
# c = a.copy(): This line creates a shallow copy of the dictionary a and assigns it to c. Now, c refers to a separate dictionary object, but with the same key-value pairs as a.
# a['name'] = 'xyz': This line modifies the value associated with the key 'name' in the dictionary a to 'xyz'.
# print(b['name'], c['name']): This line prints the values associated with the key 'name' in dictionaries b and c. Since b refers to the same dictionary object as a, it reflects the change made to a, so b['name'] will print 'xyz'. However, c refers to a separate dictionary object created with copy(), so it retains the original value 'abc'.