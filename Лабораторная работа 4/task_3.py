# TODO реализовать функцию удаления элемента из списка по индексу

def delete(list_, index=None):
    if index is None:
        index = -1
        return list_[:index]  # Если индекс не задан, то по умолчанию удаляем последний элемент
    else:
        return list_[:index] + list_[index+1:]  # Если индекс переопределён, то слайсируем, исключая нужный элемент


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 3]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
