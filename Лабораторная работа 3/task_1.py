src = not False and True or False and not True

# TODO расписать упрощение выражения

# избавляемся от отрицаний
# result = True and True or False and False

# избавляемся от "и"
# result = True or False

# избавляемся от "или"
# result = True

result = True  # TODO подставить результат выражения

print(src == result)  # True
