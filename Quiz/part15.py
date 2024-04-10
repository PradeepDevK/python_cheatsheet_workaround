alist = [5, 10, 15, 25]
print(alist[::-2]) # [25, 10]
print(alist[::-1]) # The code print(alist[::-1]) will reverse the list alist and print [25, 15, 10, 5]

# alist[::-2] is a slicing operation that starts from the end of the list (-1) and steps backwards by 2.
# So, it selects elements from the list starting from the end and moving backwards, skipping every second element.
# Therefore, it selects elements [25, 10] from the original list [5, 10, 15, 25].