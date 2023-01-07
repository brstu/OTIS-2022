Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №1 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнил: <br/>
Студент 1 курса <br/>
Группы ИИ-22(II) <br/>
Сокол С.М.<br/>

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


``` julia
using Plots
D=0.74
C=0.19
K=1.78
S=0.43
    function Linear_Model(current_y,t,warm)
        MASS_y=[]
        println("Liner date ")
        println(current_y)
        push!(MASS_y,current_y)
        for i in 1:t
            New_y=D*current_y+C*warm
            push!(MASS_y,New_y)
            current_y=New_y
            println(New_y)
        end
        plot([1:(t+1)], MASS_y, color = :blue , label = "Linear_model")
        #println("Liner date ", MASS_y)
    end
    function Unlinear_Model(middle_y,t,middle_warm)
        last_y=0
        last_warm=0
        MASS_y=[]
        println("UnLiner date ")
        println(middle_y)
        push!(MASS_y,middle_y)
        for i in 1:t
            New_y=D*middle_y-C*last_y^2+K*middle_warm+S*sin(last_warm)
            push!(MASS_y,New_y)
            last_y=middle_y
            middle_y=New_y
            last_warm=middle_warm
            middle_warm=middle_warm+0.005
            println(New_y)
        end
        plot!([1:(t+1)], MASS_y, color = :green , label = "UnLinear_model")
        savefig("tam.png")
        #println("UnLiner date ", MASS_y)
    end
    Linear_Model(0,8,2)
    Unlinear_Model(1,6,1) 
```
