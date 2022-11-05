import random


def get_unique_list_numbers(rand_a: int = -10, rand_b: int = 10, list_size: int = 15) -> list[int]:
    try:
        return random.sample(range(rand_a, rand_b + 1), list_size)
    except ValueError:
        raise ValueError('Length of generated list is less than the number of characters')


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
