<p align="center"> Министерство образования Республики Беларусь</p>
<p align="center">Учреждение образования</p>
<p align="center">“Брестский Государственный технический университет”</p>
<p align="center">Кафедра ИИТ</p>
<br><br><br><br><br><br><br>
<p align="center">Лабораторная работа №3</p>
<p align="center">По дисциплине “Общая теория интеллектуальных систем”</p>
<p align="center">Тема: “Разработка редактора графов”</p>
<br><br><br><br><br>
<p align="right">Выполнил:</p>
<p align="right">Студент 2 курса</p>
<p align="right">Группы ИИ-21</p>
<p align="right">Карагодин Д.Л.</p>
<p align="right">Проверил:</p>
<p align="right">Иванюк Д. С.</p>
<br><br><br><br>
<p align="center">Брест 2022</p>


---
# Задание: #
1. Разработать и реализовать программный продукт позволяющий
редактировать графовые конструкции различных видов и производить над
ними различные действия. Язык программирования - любой.

2. Редактор должен позволять (задания со **[\*]** являются необязательными):  
  a) одновременно работать с несколькими графами (MDI);  
  b) **[\*]** выделение одновременно нескольких элементов графа, копирование
выделенного фрагмента в clipboard и восстановление из него;  
  c) задавать имена графам;  
  d) сохранять и восстанавливать граф во внутреннем формате программы;  
  e) экспортировать и импортировать граф в текстовый формат (описание
см. ниже);  
  f) создавать, удалять, именовать, переименовывать, перемещать узлы;  
  g) создавать ориентированные и неориентированные дуги, удалять дуги;  
  h) добавлять, удалять и редактировать содержимое узла (содержимое в
виде текста и ссылки на файл);  
  i) задавать цвет дуги и узла, образ узла;  
  j) **[\*]** создавать и отображать петли;  
  k) **[\*]** создавать и отображать кратные дуги.

3. Программный продукт должен позволять выполнять следующие операции:  
    a) выводить информацию о графе:

    + количество вершин, дуг;
    + степени для всех вершин и для выбранной вершины;
    + матрицу инцидентности;
    + матрицу смежности;
    + является ли он деревом, полным, связанным, эйлеровым, **[\*]** планарным;

    b) поиск всех путей (маршрутов) между двумя узлами и кратчайших;  
    c) вычисление расстояния между двумя узлами;  
    d) вычисление диаметра, радиуса, центра графа;  
    e) **[\*]** вычисление векторного и декартово произведения двух графов;  
    f) **[\*]** раскраска графа;  
    g) нахождения эйлеровых, [*] гамильтоновых циклов;  
    h) **[\*]** поиск подграфа в графе, со всеми или некоторыми неизвестными
    узлами;  
    i) **[\*]** поиск узла по содержимому;  
    j) **[\*]** объединение, пересечение, сочетание и дополнение графов;  
    k) **[\*]** приведение произвольного графа к определенному типу с
    минимальными изменениями:

    + бинарное и обычное дерево;
    + полный граф;
    + планарный граф;
    + связанный граф;

4. Формат текстового представления графа:
<ГРАФ> ::= <ИМЯ ГРАФА> : UNORIENT | ORIENT ; <ОПИСАНИЕ УЗЛОВ> ;
<ОПИСАНИЕ СВЯЗЕЙ> .
<ИМЯ ГРАФА> ::= <ИДЕНТИФИКАТОР>
<ОПИСАНИЕ УЗЛОВ> ::= <ИМЯ УЗЛА> [ , <ИМЯ УЗЛА> …]
<ИМЯ УЗЛА> ::= <ИДЕНТИФИКАТОР>
<ОПИСАНИЕ СВЯЗЕЙ> ::= <ИМЯ УЗЛА> -> <ИМЯ УЗЛА> [ , <ИМЯ УЗЛА> …] ;
[<ОПИСАНИЕ СВЯЗЕЙ> …]

5. Написать отчет по выполненной лабораторной работе в .md формате (readme.md). Разместить его в следующем каталоге: **trunk\ii0xxyy\task_03\doc** (где **xx** - номер группы, **yy** - номер студента, например **ii02102**). 

6. Исходный код разработанной программы разместить в каталоге: **trunk\ii0xxyy\task_03\src**.

---
<br>

# Необходимые библиотеки: #
```bash
pip3 install -Iv customtkinter==4.6.3 networkx scipy 
```

---
<br>

# Описание работы программы: #
## Окно программы и создание графа
https://user-images.githubusercontent.com/51264803/207812226-b91be137-722c-497a-b755-b724d214b565.mp4

## Создаем вершины
https://user-images.githubusercontent.com/51264803/207812240-0ac4562e-7d9c-4dbc-8125-8c729720675e.mp4

## Соединяем вершины ребрами
https://user-images.githubusercontent.com/51264803/207812261-f305850f-06bb-4d69-b4df-c341e50c63ac.mp4

## Изменяем цвета вершин, ребер и передвигаем их
https://user-images.githubusercontent.com/51264803/207812269-2c329bb7-f93a-49b8-b2eb-3611da13baa2.mp4

## Удалим лишние нам вершины
https://user-images.githubusercontent.com/51264803/207812130-a8952130-ab64-4452-9355-60c09bcb8bf2.mp4

## Можем сохранить граф во внутреннем формате или экспортировать в текстовый файл
https://user-images.githubusercontent.com/51264803/207812139-298ee8c0-96cf-4dfb-a932-e0b938b3deed.mp4

## Вычислим Радиус,Диаметр,Центр графа
https://user-images.githubusercontent.com/51264803/207812154-b9063163-c4c8-408b-af89-30c79b4d5783.mp4

## Найти Эйлеров цикл для графа
https://user-images.githubusercontent.com/51264803/207812169-9e273aeb-0489-4d98-8b4e-2e9a71e86fa9.mp4

## Вычислим матрицу Дейкстры
https://user-images.githubusercontent.com/51264803/207812187-beba7d8c-3a6c-43b9-ae6d-ba429a464214.mp4

## Посмотрим общую информацию о графе
https://user-images.githubusercontent.com/51264803/207812203-f3aae780-6930-4bab-b2ea-e393d5eb909d.mp4
