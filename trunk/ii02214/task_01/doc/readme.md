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
    
    # функция для получения массива значений линейной функции y
    # для последующего построение графика с помощью библиотеки PLots
    for i in 1 : time_c  
        global  y_func = c1_first[1] * y_func + c1_first[2] * warm_1
        push!(y_mass_1, y_func) 
    end  
end

function get_y_func_second()
    # функция для получения массива значений нелинейной функции y
    # для последующего построение графика с помощью библиотеки PLots
    index = 0     
    while index < 20
        # временная переменная
        tmp = y_nonline
        global y_nonline = c2_second[1]*y_nonline - c2_second[2]*y_prev^2 + c2_second[3]*warm_1 + c2_second[4]*sin(warm_1) 
        global  y_prev = tmp
        push!(y_mass_2, y_nonline)
        index += 1
    end
end

function get_image()
    # фунция для построения графика с помощью библиотека Plots
    # строит график из массивов значений линейной и нелинейной функции
    # сохраняет картинку в текущую дирректорию
    x = range(0, time_c, length=time_c)
    plot(x, [y_mass_1, y_mass_2])
    savefig("plot.png")
end
# константные переменные для линейной функции
c1_first = [0.9, 1.4]
# констатные перменные для нелинейной функции
c2_second = [0.5, 0.4, 1, 0.7 ]
# массив выходных значений y
y_mass_2 = []
y_mass_1 = []

# предыдущий у 
y_prev = 0

y_func = 1 

warm_1 = 1
time_c = 20

function main()
    # функция main для вызова всех функций
    get_y_func_first()

    y_nonline = 1
    get_y_func_second()
    get_image()    
end
~~~

## График ##

![график](/trunk/ii02214/task_01/doc/plot.png)

