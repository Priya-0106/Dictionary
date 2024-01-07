d={'P':'Enjoy','D':'sad'}
e={0:'hello',1:'world'}
print(d)
print(e)

# update the dictionary, 'd.update(e)'
d.update(e)
print(d)

# delete the key value, used to 'del d['P']'.
del d['P']

# Print only keys.
print(d.keys())

# Print only values.
print(d.values())

# "Items" is work on print all the 'Keys' and 'Values' in separated. 
print(d.items())
