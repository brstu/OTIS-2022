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
Клебанович В.Н. <br/>

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
~~~

## График ##

![график](/trunk/ii02208/tusk_1/doc/A.png)
