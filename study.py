blood_types = ['A', 'B', 'AB', 'O', 'O', 'A', 'A', 'AB', 'AB', 'B']

# blood_dict = {}
# for blood in blood_types:
#     result = blood_types.count(blood)
#     blood_dict[blood] = result
# print(blood_dict)

blood_dict = {}
for blood in blood_types:
    if blood in blood_dict.keys():
        blood_dict[blood] +=1
    else:
        blood_dict[blood] = 1
print(blood_dict)