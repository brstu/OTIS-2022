<p align="center"> Министерство образования Республики Беларусь</p>
<p align="center">Учреждение образования</p>
<p align="center">“Брестский Государственный технический университет”</p>
<p align="center">Кафедра ИИТ</p>
<br><br><br><br><br><br><br>
<p align="center">Лабораторная работа №2</p>
<p align="center">По дисциплине “Общая теория интеллектуальных систем”</p>
<p align="center">Тема: “ПИД-регуляторы”</p>
<br><br><br><br><br>
<p align="right">Выполнил:</p>
<p align="right">Студент 2 курса</p>
<p align="right">Группы ИИ-22</p>
<p align="right">Полиенко В.Э.</p>
<p align="right">Проверил:</p>
<p align="right">Иванюк Д. С.</p>
<br><br><br><br><br>
<p align="center">Брест 2022</p>

---

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №1 в .md формате (readme.md) и с помощью запроса на внесение изменений (**pull request**) разместить его в следующем каталоге: **trunk\ii0xxyy\task_02\doc** (где **xx** - номер группы, **yy** - номер студента, например **ii02102**).
2. Исходный код написанной программы разместить в каталоге: **trunk\ii0xxyy\task_02\src**.

# Задание #
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор.  В качестве объекта управления использовать математическую модель, полученную в предыдущей работе.
В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.

---
# Код программы: #
```julia    
using Plots


#функция подсчёта линейной модели
function LinearModel(current_y, A, B, u)
    current_y = A * current_y + B * u #формула линейной модели
    return current_y
end

time = 100 #количество итераций
w = 50.0 #желаемое значение
function main()
    K = 0.09   #пропорциональная составляющая
    T = 2  #интегральная составляющая
    TD = 1.0    #дифференциальная составляющая

    To = 1      #шаг

    q0 = K * (1 + TD/To)           #
    q1 = -K * (1 + 2TD/To - To/T)  #коэффициенты для подсчёта изменения управляющего сигнала
    q2 = (K * TD)/To               #

    println("START")
    Mass_Y = [] #массив текущих значений
    Mass_U = []    #массив управляющих сигналов
    A = 0.7
    B = 0.2
    current_y = 0.0 # начально значение У
    U = 0.0
    Mass_E = [0.0, 0.0, 0.0] #массив разности желаемого значения и текущего значения
    #цикл вычисления Y для линейной модели
    for i in 1:time
        Mass_E[3] = Mass_E[2] 
        Mass_E[2] = Mass_E[1]
        Mass_E[1] = w - current_y
        U = U + q0 * Mass_E[1] + q1 * Mass_E[2] + q2 * Mass_E[3]
        current_y = LinearModel(current_y, A, B, U) #вычисление текущего значения y
        push!(Mass_Y, current_y)     #добавляем в массив текущее значение
        push!(Mass_U, U)  
        println(i, ". y = ", current_y, "\t| u = ", U)
    end
    plot(1:time, range(w, w, time), label="Target",lw=3, color=:blue, legend=:outerbottom)# Построение графиков
    plot!(1:time, Mass_U, label="Control",  color=:red)
    plot!(1:time, Mass_Y, label="Current",  color=:green)
    println("End")
end
main()
```
