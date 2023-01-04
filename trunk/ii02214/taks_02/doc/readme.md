Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №1 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнил: <br/>
Студент 2 курса <br/>
Группы ИИ-22 <br/>
Марач М.С. <br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

## Общее задание ##
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор.  В качестве объекта управления использовать математическую модель, полученную в предыдущей работе.
В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.

## Код программы ##

~~~julia
using Plots
arm_tw = 25
e_amx = [0.0,0.0,0.0]
global y_start = 0.0
c_onstant_for_function = [2,0.9]
z_u = [0.0,0.0]
vrema = 20
ka = 0.01
T = 1.1
T0 = 1
Td = 1
q0 = ka * (1  + Td/T0)
q1 = -ka * (1 + 2*Td/T0 - T0/T)  
q2 = (ka * Td)/T0
y_linear_func = []
array_u = []
function cyc_for_func()
    for i in 1 : vrema
        global y_start
        e_amx[3] = e_amx[2]
        e_amx[2] = e_amx[1]
        e_amx[1] = arm_tw - y_start
        delta_u = q0 * e_amx[1] + q1*e_amx[2] + q2*e_amx[3]
        z_u[2] = z_u[1]
        z_u[1] = z_u[2] + delta_u
        y_start = c_onstant_for_function[1] * y_start + c_onstant_for_function[2] * z_u[1]
        push!(y_linear_func ,y_start)
        push!(array_u,z_u[1])
    end 
end
function create_img()
    # функция для создания графика  
    x = range(0,vrema,length=vrema)
    plot(x,[range(arm_tw,arm_tw,vrema),y_linear_func ,array_u],Color =["blue" "green" "red"])
    savefig("plot.png")    
end
cyc_for_func()
create_img()
~~~

## График ##

![график](/trunk/ii02214/task_02/doc/plot.png)
