# python_control_structures
## Циклы while for, операторы break и continue, классы range и enumerate

## Описание/Пошаговая инструкция выполнения домашнего задания:
### 1) Пользователь вводит целое число, программа складывает все цифры числа, с полученым числом - тоже самое и так до тех пор, пока не получится однозначное число.
Пример:<br/> 
545 -> 5<br/> 
12345 -> 6<br/> 
### 2) Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0, Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется. Программа должна найти ряд, где можно приобрести нужное количество билетов (места должны быть рядом). Если таких рядов несколько то ближайший к экрану (ближайшим считается нулевой ряд). Ели таких мест нет, то вывести False
Пример:<br/> 
[[0,1,1,0],[1,0,0,0],[0,1,0,0]], 2 -> <br/> 
[[0,1,1,0],[1,0,1,0],[1,1,0,1]], 2 -> False<br/> 
### 3) Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы в коэффициент и символ.
Пример:<br/> 
aaabbbbccccc -> 2a4b5c<br/>   
asssdddsssddd -> 1a3s3d3s3d <br/>  
abcba -> 1a1b1c1b1a<br/> 
### 4) Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашфированную строку (со сдвигом по ключу). Сдвиг циклический. Используем только латинский алфавит, пробелы не шифруются.
Пример:
Dog, 2 -> Fqi  
Zak zak -> Cdn cdn  
Python is the BEST -> Udymts nx ymj GJXY
### 5) Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида: 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль Название предмета, далее список учеников и все их оценки в виде таблицы

Математика Иванов 5  
Математика Иванов 4  
Литература Иванов 3  
Математика Петров 5  
Литература Сидоров 3  
Литература Петров 5  
Литература Иванов 4  
Математика Сидоров 3  
Математика Петров 5  

Математика
Иванов 5 4
Петров 5 5
Сидоров 3

Литература
Ивванов 3 4
Сидоров 3
Петров 5
