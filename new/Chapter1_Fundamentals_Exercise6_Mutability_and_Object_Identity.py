my_list = [10, 20, 30]
print(f"Initial address: {id(my_list)}")

my_list.append(40)
print(f"After append: {id(my_list)}")
