first_list = [n for n in range(1,5)]
second_list = [n*2 for n in first_list]
# print(first_list)
# print(second_list)

names = ['Alex', 'Beth', 'Eleanor', 'Caroline', 'Fred', 'Dave', 'Angela']
long_names = [each_name.upper() for each_name in names if len(each_name) > 5]
print(names)
print(long_names)
