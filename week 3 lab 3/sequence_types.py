the_list = [234, 123, "heresy", 9+10, "spesh"]
print(len(the_list))
the_list.append(23)
the_list.insert(0, "21")
the_list.remove(23)
print(len(the_list))
print(the_list[0])
the_list[1] = 122
print(type(the_list))
the_tuple = tuple(the_list)
print(type(the_tuple))
print(the_tuple[0])
print(len(the_tuple))
#the_tuple[0] = 20
the_second_tuple = (1,2,3,4,5)
joined_tuple = the_tuple + the_second_tuple
print(joined_tuple)
the_list = list(joined_tuple)
type(the_list)
the_set = set(the_list)
len(the_set)
the_set.add(5)
print(the_set)
the_set.add(5)
print(the_set)
another_set = {1,2,3}
new_set = the_set & another_set
print(new_set)
