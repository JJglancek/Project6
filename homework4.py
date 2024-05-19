immutable_var = ([1], "tuple", False, 1.0)
print(immutable_var) # Изменение кортежа не возможно, не изменяемы вид списка
immutable_var[0][0] = 2
print(immutable_var) # Добавил в кортеж список, чтобы изменить его часть
mutable_list = [1, "list", True, 0.1]
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)
