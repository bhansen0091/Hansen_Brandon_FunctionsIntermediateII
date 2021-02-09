#1--------------------------------------------------------------------------------------------------------

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [[5, 2, 3], [10, 8, 9]]

def change_x_1(param_list):
    x[1][0] = 15
    return param_list

print(change_x_1(x))
#-----------------------------------------------------------------------------------------------------------
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
    return f"{to_find} does not exist"

print(change_name(students, "Jordan", "Bryant"))
print(change_name(students, "Michael", "Bob"))
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
    return f"{to_find} does not exist."


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
    return f"{to_find} does not exist"

print(change_z(z,20,30))
print(change_z(z,10,30))
print(change_z(z,10,1000))

# 2 --------------------------------------------------------------------------------------------------------

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(param_list):
    for param_list_dict in param_list:
        temp = ""
        for key, key_value in param_list_dict.items():
            if temp != "":
                print(f"{temp}, {key} - {key_value} ")
            else:
                temp = f"{key} - {key_value}"

iterateDictionary(students)

# 3 --------------------------------------------------------------------------------------------------------

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output 
# Michael
# John
# Mark
# KB

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(param_list, to_find):
    for list_dict in param_list:  # gets the key
        print(list_dict[to_find])

iterateDictionary2(students, "first_name")
iterateDictionary2(students, "last_name")

# 4 --------------------------------------------------------------------------------------------------------

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each 
# key along with the size of its list, and then prints the associated values within each key's list. For example:
# for key, value in param_dict.items():
#     print(f"{key}, {value}")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(param_dict):
    for key in param_dict:
        print(f"{len(param_dict[key])} {key.upper()}")
        for key_value in param_dict[key]:
            print(key_value)

print_info(dojo)