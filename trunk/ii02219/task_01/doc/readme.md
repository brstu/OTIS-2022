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
Сидоренко А.А. <br/>

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
constants = [1,0.09,1,3]
y_linear = 0
y_nonlinear_last = 0
y_current = 1
y_nonlinear  = []
warm = 1
time = 35
func = constants[1]*y_linear + constants[2] * warm
y_linear = range(func,step = func,length=time)
for i in 1 : time
    tmp = y_current
   global  y_current = constants[1] * y_current - constants[2] * y_nonlinear_last^2 + constants[3]*warm + constants[4] * sin(warm) 
   global y_nonlinear_last = tmp
   println(y_current)
   
   push!(y_nonlinear,y_current)
end
x = range(0,time,length=time)
plot(x,[y_linear,y_nonlinear],label = ["linear" "nonlinear"])
savefig("plot.png")
~~~

## График ##

![график](/trunk/ii02219/task_01/doc/plot.png)

