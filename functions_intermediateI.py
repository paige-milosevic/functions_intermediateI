"""
Exercise 1 - Update Values in dictionaries and Lists
1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
2) Change the last_name of the first student from 'Jordan' to 'Bryant'
3) In the sports_directory, change 'Messi' to 'Andres'
4) Change the value 20 in z to 30
"""

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1

list2 = x[1]
list2[0] = 15
print(x)

# 2

student1 = students[0]
student1['first_name'] = 'Bryant'
print(students)

# 3

soccer = sports_directory['soccer']
soccer[0] = 'Andres'
print(sports_directory)

#4

repository = z[0]
repository['y'] = 30
print(z)
print('')

"""
Exercise 2 - Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, 
given a list of dictionaries, the function loops through each dictionary 
in the list and prints each key and the associated value. For example, 
given the following list:
"""
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(list):
    for item in list:
        y = item['first_name']
        x = item['last_name']
        print(f'first_name - {y}, last_name - {x}')
        

iterateDictionary(students)
print('')

"""
Exercise 3 - Get Values from a List or Dictionary
Create a function iterateDictionary2(key_name, some_list) 
that, given a list of dictionaries and a key name, the function prints the 
value stored in that key for each dictionary. For example, 
iterateDictionary2('first_name', students) should output:

Michael
John
Mark
KB
"""

def iterateDictionary2(dictionary,key_name):
    for item in dictionary:
        value = item[key_name]
        print(value)

iterateDictionary2(students,'first_name')
iterateDictionary2(students,'last_name')

"""
Exercise 4 - Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose 
values are all lists, prints the name of each key along with the size 
of its list, and then prints the associated values within each key's 
list. For example:
"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dictionary):
    for item in dictionary:
        print('')
        list_len = len(dictionary[item])
        p = f'{list_len} {item}'
        print(p.upper())
        list = dictionary[item][:]
        for value in list:
            key = value[:]
            print(key)


print_info(dojo)