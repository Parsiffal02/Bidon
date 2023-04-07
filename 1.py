##1)Число N вводится с клавиатуры.
#Выведите числа перед и после данного числа так, как показано в примере. Все знаки препинания и пробелы важны.
#Входные данные
#Вводится целое число N.
#Выходные данные
#Выведите ответ на задачу так, как показано в примере:
#The next number for the number 173 is 174.
#The previous number for the number 173 is 172.
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')