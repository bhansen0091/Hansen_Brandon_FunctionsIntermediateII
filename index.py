
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [[5, 2, 3], [10, 8, 9]]


def change_x(param_list, num_to_find, num_to_sub):
    for nested_list in param_list:
        if num_to_find in nested_list:
            nested_list[nested_list.index(num_to_find)] = num_to_sub
            return param_list
    return f"Unable to locate {num_to_find}."


print(change_x(x, 10, 15))
print(change_x(x, 16, 15))
print(change_x(x, 5, 15))


# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]


def change_name(param_list, to_find, to_sub):
    for param_list_dict in param_list:
        for dict_key in param_list_dict:
            if param_list_dict[dict_key] == to_find:
                param_list_dict[dict_key] = to_sub
                return param_list
    return f"{to_find} does not exsist"


# print(change_name(students, "Jordan", "Bryant"))
# print(change_name(students, "Michael", "Bob"))
print(change_name(students, "Rosales", "Smith"))


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}


def change_name_3(param_dict, to_find, to_sub):
    for key in param_dict:
        if to_find in param_dict[key]:
            for key_value in param_dict[key]:
                if to_find in key_value:
                    param_dict[key][param_dict[key].index(key_value)] = to_sub
                    return param_dict
    return f"{to_find} does not exsist."


print(change_name_3(sports_directory, "Messi", "Andres"))
print(change_name_3(sports_directory, "James", "Not James"))
print(change_name_3(sports_directory, "Andy", "Fail"))


# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }

# def change_name_2(param_dict, to_find, to_sub):
#     for key in param_dict:  # gets the key
#         for key_value in param_dict[key]:  # gets values
#             # print(param_dict[key])
#             if to_find in key_value:
#                 param_dict[key][param_dict[key].index(key_value)] = to_sub
#                 return param_dict
#     return f"{to_find} does not exsist."

# print(change_name_2(sports_directory, "Messi", "Andres"))
# print(change_name_2(sports_directory, "James", "Not James"))
# print(change_name_2(sports_directory, "Andy", "Fail"))


# Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]

def change_z(param_list, to_find, to_sub):
    for param_list_dict in param_list:
        for dict_key in param_list_dict:
            if param_list_dict[dict_key] == to_find:
                param_list_dict[dict_key] = to_sub
                return param_list
    return f"{to_find} does not exsist"

print(change_z(z,20,30))
print(change_z(z,10,30))

