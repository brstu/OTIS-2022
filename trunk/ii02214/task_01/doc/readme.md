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

# Общее задание #
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


## Код программы ##

~~~julia
using Plots

function get_y_func_first()
    for i in 1 : time_c  
        global  y_func = constants_1[1] * y_func + constants_1[2] * warm_1
        push!(y_mass_1, y_func) 
    end  
end
function get_y_func_second()
    for i in 1 : time_c
        tmp = y_nonline
        global y_nonline = constants_2[1]*y_nonline - constants_2[2]*y_prev^2 + constants_2[3]*warm_1 + constants_2[4]*sin(warm_1) 
        global  y_prev = tmp
        push!(y_mass_2, y_nonline)
    end
end

function get_image()

    x = range(0, time_c, length=time_c)

    plot(x, [y_mass_1, y_mass_2])
    savefig("plot.png")
    
end

constants_1 = [0.9, 1.4]
constants_2 = [0.5, 0.4, 1, 0.7 ]
# массив выходных значений y
y_mass_2 = []
y_mass_1 = []

# предыдущий у 
y_prev = 0

y_func = 1 

warm_1 = 1
time_c = 20

get_y_func_first()

y_nonline = 1
get_y_func_second()
get_image()
~~~

## График ##

![график](/trunk/ii02214/task_01/doc/plot.png)

