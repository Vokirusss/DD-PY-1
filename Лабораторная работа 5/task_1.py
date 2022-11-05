from pprint import pprint

LAST_NUMBER = 15

num_list = [
    {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    for i in range(0, LAST_NUMBER + 1)
]
pprint(num_list)
