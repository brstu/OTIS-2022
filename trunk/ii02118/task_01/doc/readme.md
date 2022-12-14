<p align="center"> Министерство образования Республики Беларусь</p>
<p align="center">Учреждение образования</p>
<p align="center">“Брестский Государственный технический университет”</p>
<p align="center">Кафедра ИИТ</p>
<br><br><br><br><br><br><br>
<p align="center">Лабораторная работа №1</p>
<p align="center">По дисциплине “Общая теория интеллектуальных систем”</p>
<p align="center">Тема: “Моделирования температуры объекта”</p>
<br><br><br><br><br>
<p align="right">Выполнил:</p>
<p align="right">Студент 2 курса</p>
<p align="right">Группы ИИ-21</p>
<p align="right">Шурина А. А.</p>
<p align="right">Проверил:</p>
<p align="right">Иванюк Д. С.</p>
<br><br><br><br><br>
<p align="center">Брест 2022</p>


---
# Задание: #
1. Написать отчет по выполненной лабораторной работе №1 в .md формате (readme.md) и с помощью запроса на внесение изменений (**pull request**) разместить его в следующем каталоге: **trunk\ii0xxyy\task_01\doc** (где **xx** - номер группы, **yy** - номер студента, например **ii02102**).
2. Исходный код написанной программы разместить в каталоге: **trunk\ii0xxyy\task_01\src**.

## Task 1. Modeling controlled object ##
Let's get some object to be controlled. We want to control its temperature, which can be described by this differential equation:

$$\Large\frac{dy(\tau)}{d\tau}=\frac{u(\tau)}{C}+\frac{Y_0-y(\tau)}{RC} $$ (1)

where $\tau$ – time; $y(\tau)$ – input temperature; $u(\tau)$ – input warm; $Y_0$ – room temperature; $C,RC$ – some constants.

After transformation we get these linear (2) and nonlinear (3) models:

$$\Large y_{\tau+1}=ay_{\tau}+bu_{\tau}$$ (2)
$$\Large y_{\tau+1}=ay_{\tau}-by_{\tau-1}^2+cu_{\tau}+d\sin(u_{\tau-1})$$ (3)

where $\tau$ – time discrete moments ($1,2,3{\dots}n$); $a,b,c,d$ – some constants.

Task is to write program (**Julia**), which simulates this object temperature.


---
# Код программы #
```julia
using Plots
function linear_func(A, B, Y, U, t)
    Y = A * Y + B * U
    println(Y)
    return Y
end
function unlinear_func(A, B, C, D, Y, Y_l, U, U_l, t)
    Y = A * Y - B * Y_l * Y_l + C * U + D * sin(U_l)
    println(Y)
    return Y
end
function main()
    A = 0.479
    B = 0.533
    C = 0.651
    D = 0.032
    Y = 0.0
    U = 2.0
    N = 50
    println("Linear modeling")
    Y_linear = []
    Y_unlinear = []
    for t in 1:N
        Y = linear_func(A, B, Y, U, t)
        push!(Y_linear, Y)
    end
    println("\nUnlinear modeling") 
    Y_next = 0
    for t in 1:N
        Y_prev = Y
        Y = Y_next
        Y_next = unlinear_func(A, B, C, D, Y, Y_prev, U, U, t)
        push!(Y_unlinear, Y)
    end
    plot([1:N], Y_linear, color = :red , label = "Linear")
    plot!([1:N], Y_unlinear, color = :blue, label = "Unlinear")
    savefig("A.png")
end
main()
```
---
# Вывод #
```
Linear modeling
1.066
1.5766140000000002
1.8211981060000002
1.9383538927740003
1.9944715146387462
2.021351855511959
2.0342275387902284
2.0403949910805195
2.043349200727569
2.0447642671485053

Unlinear modeling
-0.8974079464161033
0.9012391113251084
1.3335442871021697
1.5369456094085172
1.1194390496668112
0.6082552597015213
0.954526149160659
1.5911191554175943
1.6076165427964724
0.7517709727872185
```
---
# Графики #
Линейная модель
<br>
![Линейная](images/linear.png)
<br>
