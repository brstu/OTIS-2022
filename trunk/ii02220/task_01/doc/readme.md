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
Группы ИИ-22(I) <br/>
Сиротюк Н.С. <br/>

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
function first_function(a, b, f, u)
    f = a * f + b * u
    println(f)
    return f
end
function second_function(a, b, c, d, f, f_p, u, u_p)
    f = a * f - b * f_p * f_p + c * u + d * sin(u_p)
    println(f)
    return f
end
function main()
    a = 0.722
    b = 0.421
    c = 0.587
    d = 0.035
    f = 0.0
    u = 1.0
    n = 100
    println("Linear modeling")
    f_linear = []
    f_unlinear = []
    for t in 1:n
        f = first_function(a, b, f, u)
        push!(f_linear, f)
    end
    println("\nUnlinear model")    
    f_n = 0
    for t in 1:n
        f_prev = f
        f = f_n
        f_n = second_function(a, b, c, d, f, f_prev, u, u)
        push!(f_unlinear, f)
    end
    plot([1:n], f_linear, color = :green , label = "linear")
    plot!([1:n], f_unlinear, color = :blue, label = "unlinear")
end
main()
```