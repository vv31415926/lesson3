'''
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4

Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
'''
s = input( 'Ввести числа через запятую (1 список): ' )
s = s.replace(' ','')
lst1 = s.split(',')
lst1 = list( map( int, lst1 ) )

s = input( 'Ввести числа через запятую (2 список): ' )
s = s.replace(' ','')
lst2 = s.split(',')
lst2 = list( map( int, lst2 ) )

lst=[]
for i in range( len(lst1) ):
    if lst1[i] not in lst2:
        lst.append( lst1[i] )
lst1 = lst

print( lst1 )