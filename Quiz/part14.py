my_list = [20, 40, 60]
my_list.append(80)
print(my_list) # [20, 40, 60, 80]
print(my_list.remove(20)) #None
print(my_list) # [40, 60, 80]

# my_list = [20, 40, 60]: This line initializes a list my_list containing the elements [20, 40, 60].
# my_list.append(80): This line appends the value 80 to the end of my_list. Now, my_list becomes [20, 40, 60, 80].
# print(my_list): This line prints the updated list, resulting in [20, 40, 60, 80].
# print(my_list.remove(20)): This line removes the first occurrence of 20 from my_list. The remove() method removes the element in-place and returns None. So, it prints None. After this operation, my_list becomes [40, 60, 80].