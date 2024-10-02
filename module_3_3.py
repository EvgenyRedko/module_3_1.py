def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = (5,'Привет')
values_list2 = [54.32,'Строка']
print_params(*values_list)
print_params(*values_list2)
dict_ = {5,'Всем привет', 1> 0}
print_params(*dict_)

