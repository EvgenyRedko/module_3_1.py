def print_params(a = 1, b = 'строка', c = True):
 print(a,b,c)
values_list = (5,'Привет')
values_list2 = [54.32,'Строка']
values_dict = {5,'Всем привет', 1 > 0}
print_params(*values_list)
print_params(*values_list2)
dict_ = {'a': 20, 'b': 'новая строка', 'c': True}
print_params(**dict_)
