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
w = 25
e = [0.0,0.0,0.0]
global y = 0.0
constants = [2,0.9]
u = [0.0,0.0]
time = 20
K = 0.01
T = 1.1
T0 = 1
Td = 1
q0 = K * (1  + Td/T0)
q1 = -K * (1 + 2*Td/T0 - T0/T)  
q2 = (K * Td)/T0
y_linear= []
u_mas = []
for i in 1 : time
    global y
    e[3] = e[2]
    e[2] = e[1]
    e[1] = w - y
    delta_u = q0 * e[1] + q1*e[2] + q2*e[3]
    u[2] = u[1]
    u[1] = u[2] + delta_u
    y = constants[1] * y + constants[2] * u[1]
    push!(y_linear,y)
    push!(u_mas,u[1])
end
x = range(0,time,length=time)
plot(x,[range(w,w,time),y_linear,u_mas],Color =["blue" "green" "red"])
savefig("plot.png")
~~~

## График ##

![график](/trunk/ii02219/task_02/doc/plot.png)
