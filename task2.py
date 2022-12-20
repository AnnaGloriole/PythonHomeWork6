# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

list1 = [12,'sadf',5643]
list2 = list(filter(lambda x: type(x) == int, list1))
list3 = list(filter(lambda x: type(x) == str, list1))
print('numbers in list:', *list2)
print('strings in list:', *list3)