# a = "Ежевику для ежат " \
#     "Принесли два ежа. " \
#     "Ежевику еле-еле " \
#     "Ежата возлe ели съели."
# print(len([i for i in a.split() if i.startswith('e')]))

# Python3 code to demonstrate working of
# Count of Words with specific letter
# Using filter() + lambda + len() + split()

# initializing string
test_str = "Ежевику для ежат " \
    "Принесли два ежа. " \
    "Ежевику еле-еле " \
    "Ежата возлe ели съели."

# printing original string
print(str(test_str))

# initializing letter
letter = "е"

# extracting desired count using len()
# filter() used to check for letter existence
res = len(list(filter(lambda ele: letter in ele, test_str.split())))

# printing result
print(str(res))


