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
<p style="text-align: right;">Клебанович В.Н.</p>
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
using Plots

k = 0.083
td = 0.99
t = 2
t0 = 1

Q0 = k * (1 + td/t0)
Q1 = -k * (1 + 2td/t0 - t0/t)
Q2 = (k * td)/t0

function Linear_Model(Y, koeff_a, koeff_b, U)
    Y = koeff_a * Y + koeff_b * U
    return Y
end

N = 60
n = 19.0
function main()
    ARR_linY = []
    ARR_U = []
    koeff_a = 0.78
    koeff_b = 0.42
    Y = 0.0
    previous_U = 0.0 
    U = 0.0
    delta_U = 0.0
    ARR_e = [0.0, 0.0, 0.0]

    for i in 1:N
        ARR_e[3] = ARR_e[2] 
        ARR_e[2] = ARR_e[1]
        ARR_e[1] = abs(n - Y)
        delta_U = Q0 * ARR_e[1] + Q1 * ARR_e[2] + Q2 * ARR_e[3]
        previous_U = U
        U = previous_U + delta_U
        Y = Linear_Model(Y, koeff_a, koeff_b, U)
        push!(ARR_linY, Y)
        push!(ARR_U, U)
        println(i, ". Y = ", Y, "\t U = ", U)
    end
    plot(1:N, range(n, n, N), label = "Setting", lw = 3, color = :blue, legend = :outerbottom)
    plot!(1:N, ARR_U, label = "Control Value", lw=3, color=:red)
    plot!(1:N, ARR_linY, label = "Current Value", lw = 3, color = :green)
    savefig("LAB-2.png")
end
main()
```
## График ##

![график](/trunk/ii02208/task_2/doc/LAB-2.png)
