Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №2 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «ПИД-регуляторы» <br/>

Выполнил: <br/>
Студент 2 курса <br/>
Группы ИИ-22(II) <br/>
Исаенко Н. Д. <br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №2 в .md формате (readme.md) и с помощью pull request разместить его в следующем каталоге: trunk\as000xxyy\task_02\doc.
2. Исходный код написанной программы разместить в каталоге: trunk\as000xxyy\task_02\src.

## Код программы ##

``` julia
using Plots
quantity = 100 #итерации
need = 17.6 #нужное
step = 1 #шаг

K = 0.15   #P
T = 6  #I
TD = 0.1 #D

#для упр. сигнала
q0 = K * (1 + TD/step)
q1 = -K * (1 + 2TD/step - step/T) 
q2 = (K * TD)/step

#расчёт линейной модели
function ToCalcLinearModel(y, koef_A, koef_B, u)
    return koef_A * y + koef_B * u #формула линейной модели
end

function main()
    koef_A = 0.8 
    koef_B = 1.5
    array_Y = []   #массив Y
    array_U = []    #массив U
    uPrev = 0.0 
    u = 0.0
    du = 0.0
    y = 0.0
    array_E = [0.0, 0.0, 0.0] #массив ошибок
    for i = 1:quantity
        array_E[3] = array_E[2] 
        array_E[2] = array_E[1]
        array_E[1] = abs(need - y)
        du = q0 * array_E[1] + q1 * array_E[2] + q2 * array_E[3]
        uPrev = u
        u = uPrev + du
        y = ToCalcLinearModel(y, koef_A, koef_B, u)
        push!(array_Y, y)     #добавление в массив y
        push!(array_U, u)        #добавление в массив u
    end
    plot(1:quantity, range(need, need, quantity), title="PID", label="need value", color=:red)
    plot!(1:quantity, array_U, label="Control", color=:yellow)
    plot!(1:quantity, array_Y, label="Current", color=:green)
   end
main()
```