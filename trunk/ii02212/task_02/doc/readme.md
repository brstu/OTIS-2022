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
**Задание.** На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор. В качестве объекта управления использовать математическую модель, полученную в предыдущей работе. В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.
## Код программы ##

``` julia
# program simulating PID controller
# because of the system the code was abused [2]
using Plots

value_u_t = 0.0 # control action
_this_is_a_value_time_ = 15 # time
constant_TO = 0.1 # step
this_is_a_constant_w_t = 10 # system functioning algorithm
this_is_a_constant_whanoke_a = 0.2  # constant
constant_K = 5 # transmission ratio
this_is_a_constant_karekau_b = 0.3  # constant
this_is_a_constant_uwha_c = -0.32  # constant
constant_T = 0.1# constant of integration
this_is_a_constant_tonu_d = 0.53 # constant
constant_td = 0 # constant of differentiation
array_yt_linear = [] #array for linear dependency

#function for linear dependence
function my_only_function()
    global _y_t_
    _y_t_ = 1.5 # input temperature
    _y_t_early = 0 # previous input temperature
    println("linear model")
    i = 1 # iterations
    while i <= _this_is_a_value_time_
        global value_u_t
        mistake = this_is_a_constant_w_t - _y_t_ # error
        mistake_early = mistake # previous error
        mistake_two_early = mistake_early # twice previous error
        _q_00_ = (-1)^2* (constant_K * (1 + (constant_td / constant_TO))) # controller parameters
        _q_01_ =(-1)^2* (-constant_K * (1 + 2*(constant_td / constant_TO) - (constant_TO / constant_T))) # controller parameters
        _q_02_ = (-1)^2* (constant_K * (constant_td / constant_TO)) # controller parameters
        D_value_u_t = (-1)^2* (_q_00_ * mistake + _q_01_ * mistake_early + _q_02_ * mistake_two_early) # delta control action
        u_early = value_u_t # previous control action
        value_u_t = u_early + D_value_u_t
        temperature = _y_t_early
        _y_t_ = (-1)^2*(this_is_a_constant_whanoke_a * _y_t_ + this_is_a_constant_karekau_b * value_u_t)
        _y_t_early = temperature
        println(_y_t_)
        i = i +1
        push!(array_yt_linear, _y_t_)
    end
end
# function launch
my_only_function()
# a graph is being built
plot(1:15, array_yt_linear, title = "Temperature dependence with PID controller", label = "linear dependence",  lw = 3)
```

## График ##
![](https://github.com/neonchikCallMe/OTIS-2022/blob/Lab-2/trunk/ii02212/task_02/doc/MEDuIWUodFM.jpg?raw=true) 
## Результат работы программы ##
linear model \
13.05 \
10.785 \
9.154499999999999 \
10.09665 \
10.140105 \
9.9386385 \
9.99038745 \
10.015156065 \
9.9973756905 \
9.99775607985 \
10.001198037945 \
10.000089372646501 \
9.99973358061705 \
10.000062051285585 \
10.000034668490914 
