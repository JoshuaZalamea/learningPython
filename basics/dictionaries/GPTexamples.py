# curly brackets establish the dictionary
my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

print('banana is:', my_dict['banana'])

# how to update a value in a keypair:
my_dict['banana'] = 10

# how to add a new keypair:
my_dict['pear'] = 13

print('apple is:', my_dict['apple'])
print('banana is:', my_dict['banana'])
print('pear is:', my_dict['pear'])

# how to delete a keypair:
del my_dict['apple']

print('apple' in my_dict)

# keys grabs only the keys
keys = my_dict.keys()
print('the keys are:', keys)

# values grabs only the values
values = my_dict.values()
print('the values are:', values)

# item prints all the keypairs
items = my_dict.items()
print('the items are:', items)

# get grabs the value of the key in question
banana = my_dict.get('banana')
print('banana is:', banana)

# pop grabs the value but then deletes the keypair
orange = my_dict.pop('orange')
print('orange is:', orange)
print('orange' in my_dict)

# clear empties a dictionary
my_dict.clear()
print('here are the contents of the dictionary:', my_dict)