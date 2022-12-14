<p style="text-align: center;">Министерство образования Республики Беларусь</p>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный Технический Университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №2</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “ПИД-регуляторы”</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: right;">Выполнил:</p>
<p style="text-align: right;">Студент 2 курса</p>
<p style="text-align: right;">Группы ИИ-22(I)</p>
<p style="text-align: right;">Борейша О.С.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---
## Общее задание ##
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор.  В качестве объекта управления использовать математическую модель, полученную в предыдущей работе.
В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.

---
## Код программы ##


``` julia
использование графиков

k =  0,083
td =  0,99
t =  2
t0 =  1

Q0 = k * (1  + td / t0)
Q1 = -k * (1  +  2 td / t0 - t0 / t)
Q2 = (k * td) / t0

Функция  Linear_Model(Y, koeff_a, koeff_b, U)
 Y = koeff_a * Y + koeff_b * U
    возврат Y
конец

N =  60
n =  19,0
основная  функция()
 ARR_linY = []
 ARR_U = []
 коэффициент_а =  0,78
 коэффициент b = 0,42
 Y = 0.0
 previous_U =  0.0 
 U =  0,0
 delta_U =  0,0
 ARR_e = [0.0, 0.0, 0.0]

    для i в  1: N
 ARR_e[3] = ARR_e[2] 
 ARR_e[2] = ARR_e[1]
 ARR_e[1] =  abs (n - Y)
 delta_U = Q0 * ARR_e [1] + Q1 * ARR_e [2] + Q2 * ARR_e[3]
 previous_U = U
 U = previous_U + delta_U
 Y =  Linear_Model(Y, koeff_a, koeff_b, U)
        толкай!(ARR_linY, Y)
        толкай!(ARR_U, U)
        println(i, ". Y = ", Y, "\t U = ", U)
    конец
    график (1: N, диапазон (n, n, N), метка =  "Настройка", lw =  3, цвет = : синий, легенда = : outerbottom)
    сюжет!(1: N, ARR_U, метка =  "Контрольное значение", lw = 3, цвет =: красный)
    сюжет!(1: N, ARR_linY, метка =  "Текущее значение", lw =  3, цвет = : зеленый)
    savefig("LAB-2.png")
конец
main()
```

## График: ##
![image](/trunk/ii02208/task_2/doc/LAB-2.png)
