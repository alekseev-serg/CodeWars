def remove_every_other(my_list):
    return my_list[::2]


input_list = [[1, 2]]
new_list = []

for i in range(len(input_list)):
    if i % 2:
        continue
    else:
        new_list.append(input_list[i])

print(new_list)
