Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №2 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «ПИД-регуляторы» <br/>

Выполнила: <br/>
Студент 2 курса <br/>
Группы ИИ-22(I) <br/>
Леваневская Н.И. <br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №2 в .md формате (readme.md) и с помощью pull request разместить его в следующем каталоге: **trunk\as000xxyy\task_02\doc**.
2. Исходный код написанной программы разместить в каталоге: **trunk\as000xxyy\task_02\src**.

## Task 2. ПИД-регуляторы ##
Задание. На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор. В качестве объекта управления использовать математическую модель, полученную в предыдущей работе. В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.
## Код программы ##

``` julia
# program simulating PID controller
using Plots

u = 0.0 # control action
_this_is_a_value_time_ = 15 # time
constant_To = 0.1 # step
constant_w_t = 10 # system functioning algorithm
constant_a = 0.2  # constant
constant_K = 5 # transmission ratio
constant_b = 0.3  # constant
constant_c = -0.32  # constant
constant_T = 0.1# constant of integration
constant_d = 0.53 # constant
constant_td = 0 # constant of differentiation
array_yt_linear = [] #array for linear dependency

#function for linear dependence
function f()
    global yt
    yt = 1.5 # input temperature
    yt_prev = 0 # input temperature
    println("linear model")
    for i in 1 : 15
        global u
        err = constant_w_t - yt # error
        e_early = err # previous error
        e_2early = e_early # twice previous error
        q_0 = constant_K * (1 + (constant_td / constant_To))
        q_1 = -constant_K * (1 + 2*(constant_td / constant_To) - (constant_To / constant_T))
        q_2 = constant_K * (constant_td / constant_To)
        D_u = q_0 * err + q_1 * e_early + q_2 * e_2early 
        u_early = u
        u = u_early + D_u
        temp = yt_prev
        yt = constant_a * yt + constant_b * u
        yt_prev = temp
        println(yt)
        push!(array_yt_linear, yt)
    end
end

f()
plot(1:15, array_yt_linear, title = "Temperature dependence with PID controller", label = "linear dependence",  lw = 3)
```

## График ##
image.png
## Результат работы программы ##
linear model
13.05
10.785
9.154499999999999
10.09665
10.140105
9.9386385
9.99038745
10.015156065
9.9973756905
9.99775607985
10.001198037945
10.000089372646501
9.99973358061705
10.000062051285585
10.000034668490914

 
